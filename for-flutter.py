import os

# المسار الأساسي للمشروع (يفترض أن السكريبت يُشغّل من جذر المشروع)
project_root = './'

# ملف المخرجات (Markdown)
output_file = 'mobile-code.md'

# المجلدات المستثناة (سيتم تجاهلها تماماً)
excluded_dirs = {
    'build', '.dart_tool', '.git', '.idea', '.vscode', '.gradle', '.cxx',
    '.symlinks', 'pods', 'Pods', '.ios', '.android', 'test', 'coverage',
    '.flutter-plugins-dependencies', '.metadata', '.packages', 'DerivedData'
}

# امتدادات الملفات التي نريد تضمينها (نصية وقابلة للقراءة)
included_extensions = {
    '.dart', '.yaml', '.yml', '.json', '.gradle', '.xml', '.plist', '.swift',
    '.kt', '.java', '.m', '.h', '.cpp', '.c', '.html', '.css', '.js', '.md',
    '.txt', '.sh', '.bat', '.properties', '.lock', '.gitignore', '.gitkeep',
    '.pbxproj', '.entitlements', '.strings'
}

# الحد الأقصى لحجم الملف بالميغابايت (تجنب الملفات الضخمة)
MAX_FILE_SIZE_MB = 5

def is_text_file(file_path):
    """تأكد أن الملف نصي عبر محاولة قراءة أول 1024 بايت مع utf-8"""
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            # لا يحتوي على بايتات صفرية (نصوص عادية)
            if b'\0' in chunk:
                return False
            # محاولة فك الترميز
            chunk.decode('utf-8')
            return True
    except:
        return False

def should_include_file(file_path, rel_path):
    """تحديد إذا كان الملف يجب تضمينه بناءً على الامتداد والحجم والنصية"""
    # تجنب الملفات الكبيرة جداً
    try:
        if os.path.getsize(file_path) > MAX_FILE_SIZE_MB * 1024 * 1024:
            return False
    except:
        return False

    ext = os.path.splitext(file_path)[1].lower()
    # الامتدادات المحددة مسبقاً أو اسم الملف نفسه مثل .gitignore
    if ext in included_extensions or os.path.basename(file_path) in included_extensions:
        return is_text_file(file_path)
    return False

def write_file_with_lines(out_file, file_path, rel_path):
    """كتابة الملف مع أرقام الأسطر، وتحديد لغة الكود حسب الامتداد"""
    ext = os.path.splitext(file_path)[1].lower()
    # تحديد لغة Markdown بناءً على الامتداد
    lang_map = {
        '.dart': 'dart', '.yaml': 'yaml', '.yml': 'yaml', '.json': 'json',
        '.gradle': 'gradle', '.xml': 'xml', '.plist': 'xml', '.swift': 'swift',
        '.kt': 'kotlin', '.java': 'java', '.m': 'objectivec', '.h': 'c',
        '.cpp': 'cpp', '.c': 'c', '.html': 'html', '.css': 'css', '.js': 'javascript',
        '.md': 'markdown', '.txt': 'text', '.sh': 'bash', '.bat': 'batch',
        '.properties': 'properties', '.lock': 'text', '.gitignore': 'gitignore',
        '.pbxproj': 'text', '.entitlements': 'xml', '.strings': 'text'
    }
    lang = lang_map.get(ext, 'text')
    
    out_file.write(f"## File: `{rel_path}`\n\n")
    out_file.write(f"```{lang}\n")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                # نستخدم rstrip('\n') فقط للحفاظ على المسافات
                out_file.write(f"{i} {line.rstrip(chr(10))}\n")
    except UnicodeDecodeError:
        out_file.write(f"// Warning: Could not decode file as UTF-8, skipped binary content.\n")
    except Exception as e:
        out_file.write(f"// Error reading file: {e}\n")
    out_file.write("```\n\n")

def walk_project():
    """تجميع كل الملفات المؤهلة في المشروع"""
    all_files = []
    for root, dirs, files in os.walk(project_root):
        # استبعاد المجلدات غير المرغوب فيها
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, start=project_root)
            if should_include_file(file_path, rel_path):
                all_files.append((file_path, rel_path))
    # ترتيب الملفات حسب المسار (اختياري)
    all_files.sort(key=lambda x: x[1])
    return all_files

# بدء المعالجة
with open(output_file, 'w', encoding='utf-8') as out_file:
    out_file.write("# Flutter Project Code Dump (All Important Text Files)\n\n")
    out_file.write(f"Generated from: `{os.path.abspath(project_root)}`\n\n")
    
    files_to_process = walk_project()
    total_files = len(files_to_process)
    print(f"Found {total_files} relevant text files.")
    
    for idx, (file_path, rel_path) in enumerate(files_to_process, 1):
        print(f"Processing [{idx}/{total_files}]: {rel_path}")
        write_file_with_lines(out_file, file_path, rel_path)
    
    out_file.write(f"\n# End of dump. Total files: {total_files}\n")

print(f"Done! Created {output_file} with {total_files} files.")