from pathlib import Path
import shutil
from .rules import classify

def scan_files(source_dir):
    return [f for f in source_dir.iterdir() if f.is_file()]

def build_plan(source_dir, target_dir):
    plan = []
    for f in scan_files(source_dir):
        cat = classify(f)
        dest_sub = target_dir / cat
        stem, suffix = f.stem, f.suffix
        candidate = dest_sub / (stem + suffix)
        count = 1
        while candidate.exists():
            candidate = dest_sub / f"{stem}_{count}{suffix}"
            count += 1
        plan.append((f, dest_sub, candidate.name))
    return plan

def execute_plan(plan, mode='copy', dry_run=False):
    if dry_run:
        print("[DRY RUN] 整理计划预览：")
        for src, dest_dir, name in plan:
            print(f"  {src.name} -> {dest_dir / name}")
        return
    for _, dest_dir, _ in plan:
        dest_dir.mkdir(parents=True, exist_ok=True)
    for src, dest_dir, name in plan:
        dest = dest_dir / name
        if mode == 'move':
            shutil.move(str(src), str(dest))
        else:
            shutil.copy2(str(src), str(dest))

def generate_report(plan, mode):
    if not plan:
        return
    cat_counts = {}
    for _, dest_dir, _ in plan:
        cat = dest_dir.name
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
    lines = [
        f"操作类型：{mode}",
        f"整理文件总数：{len(plan)}",
        "\n分类统计："
    ]
    for cat, cnt in cat_counts.items():
        lines.append(f"  {cat}: {cnt} 个")
    lines.append("\n详细清单：")
    for src, dest_dir, name in plan:
        lines.append(f"  {src.name} -> {dest_dir / name}")
    report_path = plan[0][1].parent / "整理报告.txt"
    report_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"整理报告已保存至：{report_path}")