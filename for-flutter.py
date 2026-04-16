import os

# المسار الأساسي للمشروع (يفترض أن السكريبت يُشغّل من جذر المشروع)
project_root = './'

# مجلد الكود الرئيسي (للتأكد من وجوده، لكننا سنبدأ المسح من الجذر)
lib_folder = os.path.join(project_root, 'lib')

# ملف pubspec.yaml (سيتم تضمينه تلقائياً من المسح العام)
pubspec_file = os.path.join(project_root, 'pubspec.yaml')

# ملف المخرجات (Markdown)
output_file = 'mobile-code.md'

# المجلدات المستثناة (لا نريد تضمين محتوياتها)
excluded_dirs = {
    'build', '.dart_tool', '.idea', '.vscode', '.git', 'node_modules',
    'android/app/build', 'ios/build', 'ios/.symlinks', 'ios/Pods',
    'macos/build', 'windows/build', 'linux/build', 'web/build',
    '.flutter-plugins', '.flutter-plugins-dependencies', '.packages'
}

# الامتدادات النصية المهمة (سيتم تضمينها)
text_extensions = {
    '.dart', '.yaml', '.yml', '.json', '.gradle', '.properties', '.xml',
    '.plist', '.swift', '.kt', '.java', '.html', '.css', '.js', '.md',
    '.txt', '.lock', '.sh', '.bat', '.cmake', '.h', '.m', '.cpp', '.c',
    '.mm', '.xcconfig', '.pbxproj', '.gradle.kts', '.proto', '.graphql'
}

# أسماء ملفات خاصة (بدون امتداد) سيتم تضمينها حتى لو لم تكن في القائمة أعلاه
special_filenames = {
    'LICENSE', 'README', 'CHANGELOG', 'CONTRIBUTING', 'AUTHORS',
    '.gitignore', '.gitattributes', '.gitmodules', '.metadata',
    'flutter_export_environment.sh', 'Podfile', 'Podfile.lock'
}

# دالة لكتابة ملف مع أرقام الأسطر (مع محاولة فك الترميز كـ UTF-8)
def write_file_with_lines(out_file, file_path, rel_path, lang):
    out_file.write(f"## File: `{rel_path}`\n\n")
    out_file.write(f"```{lang}\n")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                out_file.write(f"{i} {line.rstrip(chr(10))}\n")
    except UnicodeDecodeError:
        # تخطي الملفات الثنائية
        out_file.write(f"// Skipping binary file: {file_path}\n")
    except Exception as e:
        out_file.write(f"// Error reading file: {e}\n")
    out_file.write("```\n\n")

def get_language_from_extension(ext):
    """تحديد لغة الترميز المناسبة لعرض الكود في Markdown"""
    mapping = {
        '.dart': 'dart', '.yaml': 'yaml', '.yml': 'yaml', '.json': 'json',
        '.gradle': 'gradle', '.properties': 'properties', '.xml': 'xml',
        '.plist': 'xml', '.swift': 'swift', '.kt': 'kotlin', '.java': 'java',
        '.html': 'html', '.css': 'css', '.js': 'javascript', '.md': 'markdown',
        '.sh': 'bash', '.bat': 'batch', '.cmake': 'cmake', '.h': 'cpp',
        '.m': 'objectivec', '.cpp': 'cpp', '.c': 'c', '.mm': 'objectivec',
        '.xcconfig': 'ini', '.pbxproj': 'xml', '.gradle.kts': 'kotlin',
        '.proto': 'protobuf', '.graphql': 'graphql', '.lock': 'yaml'
    }
    return mapping.get(ext, 'text')

with open(output_file, 'w', encoding='utf-8') as out_file:
    out_file.write("# Mobile Project Code (with line numbers)\n\n")
    out_file.write("> تم إنشاؤه بواسطة سكريبت يجمع جميع الملفات النصية المهمة.\n\n")

    # المسح من جذر المشروع
    if not os.path.isdir(project_root):
        out_file.write(f"## Error: Project root `{project_root}` not found.\n\n")
    else:
        for root, dirs, files in os.walk(project_root):
            # استبعاد المجلدات غير المرغوب فيها (تعديل القائمة مباشرة)
            dirs[:] = [d for d in dirs if d not in excluded_dirs]

            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, start=project_root)

                # الحصول على الامتداد واسم الملف
                ext = os.path.splitext(file)[1].lower()
                base_name = file

                # تحديد ما إذا كان الملف مهمًا
                is_important = (
                    ext in text_extensions or
                    base_name in special_filenames or
                    # تضمين الملفات بدون امتداد ولكن قد تكون مهمة (مثل الملفات المخفية .gitignore)
                    (ext == '' and base_name.startswith('.'))
                )

                if not is_important:
                    continue

                # تحديد لغة الترميز
                lang = get_language_from_extension(ext)
                # معالجة خاصة لـ .gitignore ونحوها (لا امتداد)
                if ext == '' and base_name.startswith('.'):
                    lang = 'text'

                write_file_with_lines(out_file, file_path, rel_path, lang)

    # إذا لم يتم العثور على أي ملف، نكتب تحذيراً
    out_file.write("\n---\n*End of project files*\n")

print(f"✅ تم الإنشاء! الملف الناتج: {output_file} (يشمل جميع الملفات النصية المهمة)")