# main.py
import argparse
from pathlib import Path
from course_organizer.core import build_plan, execute_plan, generate_report

def main():
    parser = argparse.ArgumentParser(description="课程资料整理器")
    parser.add_argument('--source', required=True)
    parser.add_argument('--target', required=True)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--mode', choices=['copy','move'], default='copy')
    args = parser.parse_args()

    source = Path(args.source)
    target = Path(args.target)
    if not source.is_dir():
        print(f"错误：源目录 '{source}' 不存在。")
        return

    plan = build_plan(source, target)
    if args.dry_run:
        execute_plan(plan, mode=args.mode, dry_run=True)
    else:
        execute_plan(plan, mode=args.mode, dry_run=False)
        generate_report(plan, args.mode)

if __name__ == '__main__':
    main()