# Quick Deployment Guide - Get Your Live Link in 10 Minutes!

## 🚀 Deploy to Render.com (FREE)

Follow these simple steps to get your live deployment link:

### Step 1: Prerequisites
- GitHub account (you already have this!)
- Render.com account (free signup at https://render.com)

### Step 2: Push Your Code to GitHub
Your code is already on GitHub at: `AkashManda854/Capstone-Project`

### Step 3: Deploy on Render

1. **Go to Render Dashboard**
   - Visit https://render.com
   - Sign up or login (use GitHub login for easy integration)

2. **Create New Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect your GitHub account if not already connected
   - Select the repository: `AkashManda854/Capstone-Project`
   - Select branch: `copilot/build-festival-ecommerce-website` (or `main`)

3. **Configure Your Service**
   Fill in the following:
   ```
   Name: festival-ecommerce (or any name you prefer)
   Region: Choose closest to you
   Branch: copilot/build-festival-ecommerce-website
   Root Directory: (leave blank)
   Runtime: Python 3
   Build Command: ./build.sh
   Start Command: gunicorn festival_ecommerce.wsgi:application
   ```

4. **Add Environment Variables**
   Click "Advanced" and add these environment variables:
   ```
   SECRET_KEY = your-secret-key-here-generate-a-random-string
   DEBUG = False
   ALLOWED_HOSTS = your-app-name.onrender.com
   CSRF_TRUSTED_ORIGINS = https://your-app-name.onrender.com
   DATABASE_URL = (Render will auto-provide this if you add PostgreSQL)
   ```

   **Generate a SECRET_KEY:**
   ```python
   python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. **Add PostgreSQL Database (Optional but Recommended)**
   - In your service settings, scroll down
   - Click "Add PostgreSQL"
   - Render will automatically add DATABASE_URL environment variable

6. **Deploy!**
   - Click "Create Web Service"
   - Wait 3-5 minutes for the build to complete
   - Your app will be live at: `https://your-app-name.onrender.com`

### Step 4: Access Your Live Site

Once deployed, you'll get a URL like:
```
https://festival-ecommerce-xyz.onrender.com
```

**Default Login Credentials:**
- Admin: `admin` / `admin123`
- User: `testuser` / `test123`

### 🎉 Your Deployment Link

After deployment, update the README with your live link:
```markdown
## 🌐 Live Demo

**Deployment Link:** https://your-app-name.onrender.com
```

---

## Alternative: Deploy to Railway.app

### Quick Railway Deployment

1. Visit https://railway.app
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Choose `AkashManda854/Capstone-Project`
5. Railway auto-detects Django and deploys!
6. Add environment variables in Railway dashboard
7. Get your live link: `your-project.up.railway.app`

---

## Alternative: Deploy to PythonAnywhere

### PythonAnywhere Steps (Manual)

1. Sign up at https://www.pythonanywhere.com (free tier)
2. Open a Bash console
3. Clone your repo:
   ```bash
   git clone https://github.com/AkashManda854/Capstone-Project.git
   cd Capstone-Project
   ```
4. Create virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```
5. Configure WSGI file (PythonAnywhere provides UI)
6. Set up static files
7. Your site will be at: `yourusername.pythonanywhere.com`

---

## Troubleshooting

### Build Fails
- Check that all dependencies are in `requirements.txt`
- Verify Python version matches `runtime.txt`
- Check build logs for specific errors

### Static Files Not Loading
- Ensure `collectstatic` runs in build script
- Verify `STATIC_ROOT` is set correctly
- Check WhiteNoise is installed

### Database Issues
- For Render: Make sure PostgreSQL database is added
- Check `DATABASE_URL` environment variable is set
- Run migrations: `python manage.py migrate`

### 502 Bad Gateway
- Check that gunicorn is starting correctly
- Verify `ALLOWED_HOSTS` includes your Render URL
- Check application logs in Render dashboard

---

## Post-Deployment Checklist

After deployment, verify:
- [ ] Homepage loads correctly
- [ ] Login works
- [ ] Products display properly
- [ ] Admin panel accessible at `/admin/`
- [ ] Static files (CSS, images) load
- [ ] Database is working (create a test user)

---

## Support

If you encounter issues:
1. Check Render/Railway/PythonAnywhere logs
2. Verify all environment variables are set
3. Review the main DEPLOYMENT.md for detailed guides
4. Check Django logs for errors

---

**Need Help?** Open an issue on GitHub with your deployment logs.

**Ready to Deploy?** Start with Render.com - it's the easiest! 🚀
