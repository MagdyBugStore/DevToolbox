الملف الذي قدمته ممتاز ومنظم بشكل جيد جداً، ولكن قمت ببعض التحسينات الطفيفة لجعله أكثر احترافية، مثل:

1.  **تحسين صياغة العناوين**: جعلها أكثر وضوحاً.
2.  **إضافة كتل برمجية (Code Blocks)**: لتمييز المسارات والمتغيرات.
3.  **ترتيب الجداول**: التأكد من محاذاتها بشكل مريح للعين.
4.  **تصحيح بعض الروابط المنطقية**: التأكد من أن التعليمات تتبع تسلسلاً منطقياً.

إليك النسخة المعدلة:

---

# 🚀 Code Bundler & Project Tree Scripts

مجموعة من سكربتات Python المصممة لمشاريع (**React, Node.js, Express TS, Flutter**) لتجميع الأكواد وتوليد هيكلية المشروع في ملفات نصية سهلة القراءة، مما يسهل مشاركتها مع أدوات الذكاء الاصطناعي أو لتوثيق المشروع.

## 📋 المتطلبات الأساسية

* إصدار **Python 3.x** أو أحدث.
* إضافة Python إلى مسار النظام (**Environment Variables**).
* تثبيت **Node.js** و **npm** (خاص بمشاريع Express TS).

---

## 📦 محتويات الحزمة

| الملف | الوصف |
| :--- | :--- |
| `for-react.py` | تجميع كود React في ملف واحد. |
| `for-node.py` | تجميع كود Node.js (JavaScript). |
| `for-express-ts.py` | تهيئة مشروع Express TypeScript + MongoDB. |
| `for-flutter.py` | تجميع كود Flutter (Dart). |
| `get-root-file.py` | توليد شجرة المجلدات (Directory Tree). |
| `init-backend/` | أداة متكاملة لتهيئة مشاريع Express TS. |

---

## 💻 إعداد الاختصارات (Setup Shortcuts)

للوصول للسكربتات من أي مكان في الجهاز، يفضل إعداد الاختصارات التالية:

### 🪟 Windows (PowerShell)
1. افتح PowerShell واكتب الأمر التالي لفتح ملف الإعدادات:
   ```powershell
   notepad $PROFILE
   ```
2. أضف الأوامر التالية (مع استبدال `C:\Scripts` بالمسار الفعلي الذي وضعت فيه الملفات):
   ```powershell
   function bundle-react { python "C:\Scripts\for-react.py" }
   function bundle-node { python "C:\Scripts\for-node.py" }
   function init-backend { python "C:\Scripts\init-backend\init-backend.py" }
   function bundle-flutter { python "C:\Scripts\for-flutter.py" }
   function get-tree { python "C:\Scripts\get-root-file.py" }
   
   # تعريف الأسماء المستعارة (Aliases)
   Set-Alias br bundle-react
   Set-Alias bn bundle-node
   Set-Alias ib init-backend
   Set-Alias bf bundle-flutter
   Set-Alias gt get-tree
   ```

### 🍎 macOS & 🐧 Linux
1. افتح ملف الإعدادات الخاص بالـ Terminal (غالباً `~/.zshrc` أو `~/.bashrc`):
   ```bash
   nano ~/.zshrc
   ```
2. أضف الـ Aliases التالية في نهاية الملف:
   ```bash
   alias br='python3 /path/to/scripts/for-react.py'
   alias bn='python3 /path/to/scripts/for-node.py'
   alias ib='python3 /path/to/scripts/init-backend/init-backend.py'
   alias bf='python3 /path/to/scripts/for-flutter.py'
   alias gt='python3 /path/to/scripts/get-root-file.py'
   ```
3. احفظ الملف ثم نفذ `source ~/.zshrc` لتفعيل التغييرات.

---

## 🛠️ كيفية الاستخدام (Usage)

| الأمر | الوصف | ملف المخرجات |
| :--- | :--- | :--- |
| `br` | تجميع كود **React** | `react_code.txt` |
| `bn` | تجميع كود **Node.js** | `node_code.txt` |
| `ib` | **تهيئة مشروع Express TypeScript** | هيكل مشروع متكامل |
| `bf` | تجميع كود **Flutter** | `mobile-code.txt` |
| `gt` | توليد شجرة المجلدات | `app-root.md` |

---

## 🚀 تهيئة مشروع Express TypeScript + MongoDB

أداة متكاملة لإنشاء مشروع Node.js احترافي باستخدام TypeScript مع MongoDB.

### ✨ المميزات
- **هيكل مجلدات منظم**: (config, controllers, middleware, models, routes, services, utils).
- **نظام مصادقة**: تسجيل مستخدمين (Register/Login) باستخدام **JWT**.
- **الأمان**: تشفير كلمات المرور باستخدام **Bcrypt**.
- **قاعدة البيانات**: اتصال جاهز بـ MongoDB عبر Mongoose.
- **الإضافات**: معالجة الأخطاء مركزياً، والتحقق من الصلاحيات (Middleware).

### 🚀 التشغيل
```bash
# تشغيل أداة التهيئة
ib

# اتبع التعليمات في الـ Terminal
? Project name (default: express-ts-mongo): my-awesome-api
? Run 'npm install' now? (Y/n): Y

# بعد انتهاء التنفيذ
cd my-awesome-api
cp .env.example .env
# قم بتعديل MONGO_URI و JWT_SECRET في ملف .env
npm run dev
```

### 📂 هيكل المشروع الناتج
```text
my-awesome-api/
├── src/
│   ├── config/      # إعدادات قاعدة البيانات والبيئة
│   ├── controllers/ # الدوال المنطقية للطلبات
│   ├── middleware/  # حماية المسارات (Auth)
│   ├── models/      # نماذج البيانات (Mongoose)
│   ├── routes/      # تعريف مسارات الـ API
│   ├── services/    # منطق الأعمال الأساسي
│   ├── utils/       # دوال مساعدة عامة
│   ├── app.ts       # تهيئة تطبيق Express
│   └── server.ts    # تشغيل السيرفر (Entry Point)
├── .env.example     # نموذج لمتغيرات البيئة
├── tsconfig.json    # إعدادات لغة TypeScript
└── package.json     # المكتبات والسكربتات
```

---

## 📝 أمثلة سريعة

**تجميع كود React:**
```bash
cd my-react-project
br
```

**توليد شجرة المجلدات:**
```bash
gt
```

---

## 🤝 المساهمة (Contribution)
يمكنك تعديل السكربتات لتناسب احتياجاتك، مثل إضافة امتدادات ملفات جديدة لقائمة التجاهل أو تعديل قوالب الأكواد داخل مجلد `init-backend/templates/`.

---

## 📄 الترخيص
هذا المشروع مفتوح المصدر ومتاح للاستخدام الشخصي والتجاري.

**Happy Coding!** 🚀
