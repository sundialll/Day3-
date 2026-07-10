KEYWORDS = ['作业', '练习', '实验', '任务']
EXT_MAP = {
    'slides':   {'.ppt', '.pptx', '.key'},
    'code':     {'.py', '.ipynb', '.c', '.cpp', '.java'},
    'data':     {'.csv', '.xlsx', '.json'},
    'documents':{'.pdf', '.doc', '.docx', '.txt', '.md'},
    'images':   {'.png', '.jpg', '.jpeg', '.gif'},
}

def classify(file_path):
    # file_path 是 Path 对象，取其文件名用于关键字匹配
    name = file_path.name
    for kw in KEYWORDS:
        if kw in name:               
            return 'homework'
    suffix = file_path.suffix.lower() # Path 对象的 suffix 属性仍可用
    for cat, exts in EXT_MAP.items():
        if suffix in exts:
            return cat
    return 'others'