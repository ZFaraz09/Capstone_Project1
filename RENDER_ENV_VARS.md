# Environment Variables for Render.com Deployment

## Copy-Paste Ready Configuration

**IMPORTANT:** Replace `YOUR-SERVICE-NAME` with your actual Render service name!

---

### Required Environment Variables:

```
SECRET_KEY
Value: (Click "Generate" button in Render UI)

DEBUG
Value: False

PYTHON_VERSION
Value: 3.12.3

ALLOWED_HOSTS
Value: YOUR-SERVICE-NAME.onrender.com

CSRF_TRUSTED_ORIGINS
Value: https://YOUR-SERVICE-NAME.onrender.com
```

---

### Database (Auto-provided):

```
DATABASE_URL
Value: (Automatically added when you create PostgreSQL database)
```

---

## Example with Actual Service Name:

If your service name is `capstone-project`:

```
SECRET_KEY = django-insecure-v8sk33l-@lwwfr6^f2$8^cjjro3*f(1234567890)
DEBUG = False
PYTHON_VERSION = 3.12.3
ALLOWED_HOSTS = capstone-project.onrender.com
CSRF_TRUSTED_ORIGINS = https://capstone-project.onrender.com
```

---

## How to Add in Render UI:

1. Scroll to "Environment Variables" section
2. Click "Add Environment Variable"
3. Enter NAME and VALUE for each variable above
4. For SECRET_KEY, use the "Generate" button
5. Click "Create Web Service"

---

## After First Deployment:

1. Go to your service dashboard
2. Click "New +" → "PostgreSQL"
3. Select "Free" plan
4. Render will automatically add DATABASE_URL
5. Service will redeploy automatically

---

**Your deployment will be live at:**
```
https://YOUR-SERVICE-NAME.onrender.com
```

**Login with:**
- Admin: `admin` / `admin123`
- User: `testuser` / `test123`
