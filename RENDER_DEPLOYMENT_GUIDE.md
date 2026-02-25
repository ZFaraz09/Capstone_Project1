# 🎯 RENDER.COM DEPLOYMENT CONFIGURATION

## You're on the Render Deployment Page - Here's What to Configure

### ✅ STEP-BY-STEP CONFIGURATION

---

## 1️⃣ Basic Settings

**Name:** `Capstone-Project` or `festival-ecommerce` (your choice)

**Project:** Leave empty or create new project (optional)

**Branch:** `copilot/build-festival-ecommerce-website` (or `main` if merged)

**Region:** `Oregon (US West)` ✅ (Already selected - good!)

**Root Directory:** Leave **EMPTY** (blank)

---

## 2️⃣ Language/Runtime Settings

⚠️ **IMPORTANT: Change from Docker to Python!**

**Language:** Select **`Python`** (NOT Docker)

**Build Command:** 
```
./build.sh
```

**Start Command:**
```
gunicorn festival_ecommerce.wsgi:application
```

---

## 3️⃣ Instance Type

**Selected:** `Free` ✅ Good for testing!

**Note:** Free tier spins down after 15 minutes of inactivity. For production, consider Starter ($7/month) for always-on service.

---

## 4️⃣ Environment Variables (MOST IMPORTANT!)

Click **"Add Environment Variable"** for each of these:

### Required Variables:

#### 1. SECRET_KEY
```
NAME: SECRET_KEY
VALUE: (Click "Generate" button to auto-generate)
```
**Or generate manually:**
```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### 2. DEBUG
```
NAME: DEBUG
VALUE: False
```

#### 3. PYTHON_VERSION
```
NAME: PYTHON_VERSION
VALUE: 3.12.3
```

#### 4. ALLOWED_HOSTS
```
NAME: ALLOWED_HOSTS
VALUE: capstone-project.onrender.com
```
⚠️ **IMPORTANT:** Replace `capstone-project` with YOUR actual service name from step 1!

#### 5. CSRF_TRUSTED_ORIGINS
```
NAME: CSRF_TRUSTED_ORIGINS
VALUE: https://capstone-project.onrender.com
```
⚠️ **IMPORTANT:** Replace with YOUR actual URL (include `https://`)!

### Optional but Recommended:

#### 6. DATABASE_URL
```
Will be AUTO-PROVIDED when you add PostgreSQL database
```
**How to add PostgreSQL:**
- After creating the web service, go to service settings
- Click "New +" → "PostgreSQL"
- Render will automatically link it and provide DATABASE_URL

---

## 5️⃣ Summary of All Environment Variables

Copy these to Render (adjust URLs to your service name):

```
SECRET_KEY = (use Generate button)
DEBUG = False
PYTHON_VERSION = 3.12.3
ALLOWED_HOSTS = capstone-project.onrender.com
CSRF_TRUSTED_ORIGINS = https://capstone-project.onrender.com
```

**DATABASE_URL will be added automatically when you create PostgreSQL database**

---

## 6️⃣ After Configuration

1. **Review all settings**
2. Click **"Create Web Service"**
3. Wait 5-10 minutes for build
4. **Add PostgreSQL database:**
   - Go to Dashboard → Your service
   - Click "New +" → "PostgreSQL"
   - Select "Free" plan
   - Connect to your web service
5. **Your live link will be:**
   ```
   https://capstone-project.onrender.com
   ```
   (or whatever name you chose)

---

## 7️⃣ What Happens During Build

The `build.sh` script will automatically:
- ✅ Install all dependencies from requirements.txt
- ✅ Run database migrations
- ✅ Collect static files
- ✅ Create superuser (admin/admin123)
- ✅ Populate sample data (festivals, products, etc.)

---

## 8️⃣ After Deployment

### Access Your Live Site:
```
https://your-service-name.onrender.com
```

### Login Credentials:
- **Admin:** `admin` / `admin123`
- **User:** `testuser` / `test123`

### What You'll See:
- ✅ Festival-themed e-commerce homepage
- ✅ 8 sample products
- ✅ Working shopping cart
- ✅ Admin panel at `/admin/`
- ✅ REST API at `/api/`

---

## 9️⃣ Troubleshooting

### If Build Fails:
1. Check build logs in Render dashboard
2. Verify branch name is correct
3. Ensure Language is set to **Python** (not Docker)
4. Verify build command: `./build.sh`

### If Site Doesn't Load:
1. Check `ALLOWED_HOSTS` matches your Render URL
2. Verify `CSRF_TRUSTED_ORIGINS` includes `https://`
3. Check application logs
4. Ensure PostgreSQL database is connected

### If Static Files Missing:
1. Verify build logs show "collectstatic" ran
2. Check WhiteNoise is installed (it is in requirements.txt)
3. Redeploy if needed

---

## 🎯 Quick Checklist

Before clicking "Create Web Service":

- [ ] Language set to **Python** (not Docker)
- [ ] Build Command: `./build.sh`
- [ ] Start Command: `gunicorn festival_ecommerce.wsgi:application`
- [ ] Branch: correct branch selected
- [ ] SECRET_KEY: generated
- [ ] DEBUG: False
- [ ] PYTHON_VERSION: 3.12.3
- [ ] ALLOWED_HOSTS: your-service-name.onrender.com
- [ ] CSRF_TRUSTED_ORIGINS: https://your-service-name.onrender.com
- [ ] Instance Type: Free (or higher)

---

## 🎉 Success!

After deployment completes (5-10 minutes), you'll have:

✅ **Your Live Deployment Link!**
✅ Working e-commerce website
✅ Database with sample data
✅ Admin dashboard access
✅ Ready to customize and use

---

**Need Help?** Check the Render logs or refer to DEPLOYMENT.md for troubleshooting!

**Your deployment link will be ready soon! 🚀**
