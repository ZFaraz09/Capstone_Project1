# 🔑 THE 5 ENVIRONMENT VARIABLES FOR RENDER

## Quick Answer - Copy These Exactly:

### Variable 1: SECRET_KEY
```
NAME:  SECRET_KEY
VALUE: (Click "Generate" button in Render - it will create a secure random key)
```
**OR manually use:**
```
django-insecure-a$b2c!3d@4e#5f^6g&7h*8i(9j)0k-1l_2m=3n+4o~5p
```
(Replace with your own random string - at least 50 characters)

---

### Variable 2: DEBUG
```
NAME:  DEBUG
VALUE: False
```
⚠️ Must be exactly `False` (capital F)

---

### Variable 3: PYTHON_VERSION
```
NAME:  PYTHON_VERSION
VALUE: 3.12.3
```

---

### Variable 4: ALLOWED_HOSTS
```
NAME:  ALLOWED_HOSTS
VALUE: YOUR-SERVICE-NAME.onrender.com
```
⚠️ **IMPORTANT:** Replace `YOUR-SERVICE-NAME` with the actual name you entered in "Name" field!

**Example:** If your service name is `capstone-project`, use:
```
capstone-project.onrender.com
```

---

### Variable 5: CSRF_TRUSTED_ORIGINS
```
NAME:  CSRF_TRUSTED_ORIGINS
VALUE: https://YOUR-SERVICE-NAME.onrender.com
```
⚠️ **IMPORTANT:** 
- Replace `YOUR-SERVICE-NAME` with your actual service name
- Must include `https://` at the beginning!

**Example:** If your service name is `capstone-project`, use:
```
https://capstone-project.onrender.com
```

---

## 📋 Copy-Paste Format for Render Form

If your service name is `capstone-project`:

| Variable # | NAME | VALUE |
|------------|------|-------|
| 1 | `SECRET_KEY` | (Click Generate) |
| 2 | `DEBUG` | `False` |
| 3 | `PYTHON_VERSION` | `3.12.3` |
| 4 | `ALLOWED_HOSTS` | `capstone-project.onrender.com` |
| 5 | `CSRF_TRUSTED_ORIGINS` | `https://capstone-project.onrender.com` |

---

## 🎯 How to Add These in Render:

1. Scroll down to "Environment Variables" section
2. Click "Add Environment Variable" button
3. Enter NAME (from left column above)
4. Enter VALUE (from right column above)
5. Repeat for all 5 variables
6. Click "Create Web Service"

---

## ⚠️ CRITICAL NOTES:

- **SECRET_KEY**: Use Render's "Generate" button (easiest and most secure)
- **DEBUG**: Must be `False` (not "false" or "FALSE")
- **PYTHON_VERSION**: Exactly `3.12.3`
- **YOUR-SERVICE-NAME**: Whatever you typed in the "Name" field at the top of the form
- **https://**: Don't forget the `https://` in CSRF_TRUSTED_ORIGINS!

---

## ✅ After Adding These 5:

You're ready to deploy! Click "Create Web Service" and wait 5-10 minutes.

**Your live site will be at:**
```
https://YOUR-SERVICE-NAME.onrender.com
```

**Login with:**
- Admin: `admin` / `admin123`
- Test User: `testuser` / `test123`

---

## 🗄️ Database (6th Variable - Added Later)

After deployment completes:
1. Go to your service dashboard
2. Click "New +" → "PostgreSQL"
3. Select "Free" plan
4. Render automatically adds:
   ```
   DATABASE_URL = (auto-generated connection string)
   ```

---

**That's it! These are the 5 environment variables you need! 🚀**
