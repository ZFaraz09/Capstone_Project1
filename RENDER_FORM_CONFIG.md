# 🎯 RENDER FORM CONFIGURATION - Exact Details

## Quick Answer: What to Enter in Render Form

You asked: **"what details do i need to enter into render to deploy give me"**

Here's exactly what you need to enter in each field:

---

## 📋 FORM CONFIGURATION

### Current Values (Already Correct ✅)

```
Name:     Capstone-Project-3
Branch:   copilot/build-festival-ecommerce-website  
Language: Python 3
Region:   Oregon (US West)
Instance: Free
```

### Values to CHANGE ⚠️

#### 1. Build Command
**Currently says:** `pip install -r requirements.txt`

**Change to:** 
```bash
./build.sh
```

#### 2. Start Command
**Currently says:** `gunicorn your_application.wsgi`

**Change to:**
```bash
gunicorn festival_ecommerce.wsgi:application
```

---

## 🔑 ENVIRONMENT VARIABLES TO ADD

Click "Add Environment Variable" button and add these **5 variables**:

### Variable 1: SECRET_KEY
```
Key:   SECRET_KEY
Value: (Click the "Generate" button in Render UI)
```
**Note:** Render has a "Generate" button next to the value field. Click it!

### Variable 2: DEBUG
```
Key:   DEBUG
Value: False
```
**Important:** Use capital `F` in `False`

### Variable 3: PYTHON_VERSION
```
Key:   PYTHON_VERSION
Value: 3.12.3
```

### Variable 4: ALLOWED_HOSTS
```
Key:   ALLOWED_HOSTS
Value: capstone-project-3.onrender.com
```
**Important:** Replace with your actual service name if different

### Variable 5: CSRF_TRUSTED_ORIGINS
```
Key:   CSRF_TRUSTED_ORIGINS
Value: https://capstone-project-3.onrender.com
```
**Important:** Must include `https://` at the beginning!

---

## 📝 STEP-BY-STEP INSTRUCTIONS

### Step 1: Update Build Command
1. Find the "Build Command" field
2. Delete: `pip install -r requirements.txt`
3. Type: `./build.sh`

### Step 2: Update Start Command
1. Find the "Start Command" field
2. Delete: `gunicorn your_application.wsgi`
3. Type: `gunicorn festival_ecommerce.wsgi:application`

### Step 3: Add Environment Variables

For each variable below, click "Add Environment Variable":

**Add Variable 1:**
- Key: `SECRET_KEY`
- Value: Click "Generate" button (or paste a random 50+ character string)

**Add Variable 2:**
- Key: `DEBUG`
- Value: `False`

**Add Variable 3:**
- Key: `PYTHON_VERSION`
- Value: `3.12.3`

**Add Variable 4:**
- Key: `ALLOWED_HOSTS`
- Value: `capstone-project-3.onrender.com`

**Add Variable 5:**
- Key: `CSRF_TRUSTED_ORIGINS`
- Value: `https://capstone-project-3.onrender.com`

### Step 4: Create Web Service
1. Click the blue "Create Web Service" button at the bottom
2. Wait while Render builds your app (5-10 minutes)
3. Watch the build logs for any errors

### Step 5: Add PostgreSQL Database (After Initial Deploy)
1. Go back to Render Dashboard
2. Click "New +" button
3. Select "PostgreSQL"
4. Name: `capstone-project-db`
5. Region: Same as web service (Oregon)
6. Create Database
7. In database settings, find "Connect to" section
8. Select your web service `capstone-project-3`
9. Your service will automatically redeploy with DATABASE_URL

---

## ✅ COMPLETE CHECKLIST

Copy this and check off as you go:

**Form Fields:**
- [ ] Name: `Capstone-Project-3`
- [ ] Branch: `copilot/build-festival-ecommerce-website`
- [ ] Language: `Python 3`
- [ ] Build Command: `./build.sh`
- [ ] Start Command: `gunicorn festival_ecommerce.wsgi:application`

**Environment Variables:**
- [ ] SECRET_KEY (generated)
- [ ] DEBUG = False
- [ ] PYTHON_VERSION = 3.12.3
- [ ] ALLOWED_HOSTS = capstone-project-3.onrender.com
- [ ] CSRF_TRUSTED_ORIGINS = https://capstone-project-3.onrender.com

**Actions:**
- [ ] Click "Create Web Service"
- [ ] Wait for build to complete
- [ ] Verify service is live
- [ ] Add PostgreSQL database
- [ ] Test website functionality

---

## 🎯 COPY-PASTE READY FORMAT

### Build Command:
```
./build.sh
```

### Start Command:
```
gunicorn festival_ecommerce.wsgi:application
```

### Environment Variables:
```
SECRET_KEY = (use Generate button)
DEBUG = False
PYTHON_VERSION = 3.12.3
ALLOWED_HOSTS = capstone-project-3.onrender.com
CSRF_TRUSTED_ORIGINS = https://capstone-project-3.onrender.com
```

---

## ⚠️ CRITICAL NOTES

### Why ./build.sh and not pip install?
- `./build.sh` is a script that does EVERYTHING:
  - Installs dependencies (pip install)
  - Runs database migrations
  - Collects static files
  - Creates admin user (admin/admin123)
  - Populates sample data
- It's much better than just `pip install`

### Why festival_ecommerce?
- `festival_ecommerce` is the name of your Django project
- It's the folder containing your `settings.py` and `wsgi.py`
- Don't change it to anything else!

### Why include https:// in CSRF_TRUSTED_ORIGINS?
- Django requires the full URL with protocol
- Without https://, you'll get CSRF errors
- This is a security feature

### What if my service name is different?
- If you named your service something other than `Capstone-Project-3`
- Your URL will be: `https://YOUR-SERVICE-NAME.onrender.com`
- Use YOUR-SERVICE-NAME in ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS
- Example: If name is "my-shop", use:
  - ALLOWED_HOSTS = `my-shop.onrender.com`
  - CSRF_TRUSTED_ORIGINS = `https://my-shop.onrender.com`

---

## 📊 EXPECTED BUILD LOGS

After clicking "Create Web Service", you should see:

```
==> It looks like we don't have access to your repo, but we'll try to clone it anyway.
==> Cloning from https://github.com/AkashManda854/Capstone-Project
==> Checking out branch copilot/build-festival-ecommerce-website
==> Installing Python version 3.12.3
==> Using Python version 3.12.3
==> Running build command './build.sh'

Installing dependencies from requirements.txt...
Collecting setuptools>=68.0.0
Collecting Django==4.2.26
...
Successfully installed all packages

Collecting static files...
120 static files copied

Running migrations...
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, shop, accounts
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
  All migrations applied successfully

Creating superuser...
Superuser created

Populating sample data...
Creating festivals...
Creating categories...
Creating products...
Sample data populated successfully

==> Build succeeded ✓

==> Starting service with 'gunicorn festival_ecommerce.wsgi:application'
==> Your service is live at https://capstone-project-3.onrender.com
```

---

## 🔴 COMMON ERRORS & SOLUTIONS

### Error: "No such file or directory: ./build.sh"
**Cause:** Build command is wrong or branch is wrong
**Solution:** 
- Verify Build Command is exactly: `./build.sh`
- Verify Branch is: `copilot/build-festival-ecommerce-website`

### Error: "ModuleNotFoundError: No module named 'festival_ecommerce'"
**Cause:** Start command is wrong
**Solution:** Change Start Command to: `gunicorn festival_ecommerce.wsgi:application`

### Error: "DisallowedHost at /"
**Cause:** ALLOWED_HOSTS doesn't match your URL
**Solution:** 
- Check your actual service URL
- Update ALLOWED_HOSTS to match (without https://)

### Error: "Forbidden (403) CSRF verification failed"
**Cause:** CSRF_TRUSTED_ORIGINS missing or wrong
**Solution:** 
- Make sure CSRF_TRUSTED_ORIGINS includes `https://`
- Make sure it matches your service URL

---

## 🎉 AFTER SUCCESSFUL DEPLOYMENT

### Test Your Site

1. **Visit your URL:**
   ```
   https://capstone-project-3.onrender.com
   ```

2. **You should see:**
   - Festival-themed homepage (Dussehra theme with orange colors)
   - Search bar in navbar
   - Featured products with images
   - Trending products section
   - Festival selector dropdown

3. **Test login:**
   - Click "Login" in navbar
   - Username: `admin`
   - Password: `admin123`
   - Should log you in successfully

4. **Test admin panel:**
   ```
   https://capstone-project-3.onrender.com/admin/
   ```
   - Username: `admin`
   - Password: `admin123`
   - Should show Django admin interface

5. **Test search:**
   - Type "saree" in search box
   - Should show Traditional Silk Saree product
   - Product should have image

6. **Test API:**
   ```
   https://capstone-project-3.onrender.com/api/products/
   ```
   - Should show JSON list of products

---

## 💡 ADDITIONAL TIPS

### First Deployment
- Takes 5-10 minutes for initial build
- Subsequent deploys are faster (2-3 minutes)
- Free tier: Service sleeps after 15 min inactivity
- First request after sleep takes ~30 seconds

### PostgreSQL Database
- Not required immediately
- SQLite works for testing
- Add PostgreSQL for production data persistence
- Free tier PostgreSQL available

### Monitoring
- Check "Logs" tab in Render dashboard
- See real-time server logs
- Debug any issues

### Updates
- Push to GitHub branch
- Render auto-deploys changes
- No need to manually redeploy

---

## 📞 SUPPORT

**If deployment fails:**
1. Check build logs in Render dashboard
2. Verify all environment variables are correct
3. Verify Build and Start commands match exactly
4. Check branch name is correct
5. Review error messages carefully

**Documentation:**
- This file: Quick reference
- RENDER_DEPLOYMENT_GUIDE.md: Complete guide
- RENDER_ENV_VARS.md: Variable details
- FIXES_COMPLETE.md: Recent updates

---

## 🎯 SUMMARY

**To deploy, you need to enter:**

✅ **Build Command:** `./build.sh`

✅ **Start Command:** `gunicorn festival_ecommerce.wsgi:application`

✅ **5 Environment Variables:**
1. SECRET_KEY (use Generate button)
2. DEBUG = False
3. PYTHON_VERSION = 3.12.3
4. ALLOWED_HOSTS = capstone-project-3.onrender.com
5. CSRF_TRUSTED_ORIGINS = https://capstone-project-3.onrender.com

**Then:** Click "Create Web Service" and wait!

**Time:** ~15 minutes total (5 min form + 10 min build)

**Result:** Live website at https://capstone-project-3.onrender.com

---

**You're ready to deploy! Just fill in the form and click create! 🚀**
