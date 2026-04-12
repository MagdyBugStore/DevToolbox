# 🚀 Code Bundler & Project Tree Scripts

مجموعة من سكربتات Python المصممة لمشاريع (React, Node.js, Flutter) لتجميع الأكواد وتوليد هيكلية المشروع في ملفات نصية سهلة القراءة.

## 📋 المتطلبات الأساسية
* [cite_start]يجب تثبيت **Python 3.x** على جهازك[cite: 1, 8].
* تأكد من إضافة Python إلى مسار النظام (Environment Variables).

---

## 💻 إعداد الاختصارات (Setup Shortcuts)

### 🪟 Windows (PowerShell)
1. افتح PowerShell واكتب:
   ```powershell
   notepad $PROFILE
   ```
2. أضف الأوامر التالية (مع تعديل المسار `C:\Scripts` للمكان الفعلي للملفات):
   ```powershell
   function bundle-react { python "C:\DevToolbox\for-react.py" }
   function bundle-node { python "C:\DevToolbox\for-node.py" }
   function bundle-flutter { python "C:\DevToolbox\for-flutter.py" }
   function get-tree { python "C:\DevToolbox\get-root-file.py" }
   
   # اختصارات سريعة
   Set-Alias br bundle-react
   Set-Alias bn bundle-node
   Set-Alias bf bundle-flutter
   Set-Alias gt get-tree
   ```

---

### 🍎 macOS & 🐧 Linux
1. افتح ملف الإعدادات (`~/.zshrc` أو `~/.bashrc`):
   ```bash
   nano ~/.zshrc
   ```
2. أضف الـ Aliases التالية:
   ```bash
   alias br='python3 /path/to/DevToolbox/for-react.py'
   alias bn='python3 /path/to/DevToolbox/for-node.py'
   alias bf='python3 /path/to/DevToolbox/for-flutter.py'
   alias gt='python3 /path/to/DevToolbox/get-root-file.py'
   ```

---

## 🛠️ كيفية الاستخدام (Usage)

| الأمر | الوصف | ملف المخرجات |
| :--- | :--- | :--- |
| `br` | تجميع كود **React** | `react_code.txt` |
| `bn` | تجميع كود **Node.js** | `node_code.txt` |
| `bf` | تجميع كود **Flutter** | `mobile-code.txt` |
| `gt` | [cite_start]توليد شجرة مجلدات المشروع مع التعليقات [cite: 4, 6] | [cite_start]`app-root.md` [cite: 9] |

---
**Happy Coding!** 🚀
