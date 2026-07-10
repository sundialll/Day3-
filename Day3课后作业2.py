# course_organizer/rules.py
KEYWORDS = ['作业', '练习', '实验', '任务']
EXT_MAP = {
    'slides': {'.ppt', '.pptx', '.key'},
    'code': {'.py', '.ipynb', '.c', '.cpp', '.java'},
    'data': {'.csv', '.xlsx', '.json'},
    'documents': {'.pdf', '.doc', '.docx', '.txt', '.md'},
    'images': {'.png', '.jpg', '.jpeg', '.gif'},
}

def classify(name: str) -> str:
    for kw in KEYWORDS:
        if kw in name:
            return 'homework'
    suffix = name.suffix.lower()
    for cat, exts in EXT_MAP.items():
        if suffix in exts:
            return cat
    return 'others'