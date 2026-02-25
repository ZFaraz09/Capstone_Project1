# 🚀 GET YOUR LIVE DEPLOYMENT LINK NOW!

## One-Click Deploy to Render.com (FREE)

Click the button below to deploy this Festival E-Commerce Website instantly:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/AkashManda854/Capstone-Project)

---

## Manual Deployment (5-10 minutes)

### Option 1: Render.com (Recommended)

1. **Sign Up/Login to Render**
   - Go to https://render.com
   - Sign up with GitHub (easiest)

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `AkashManda854/Capstone-Project`
   - Select branch: `copilot/build-festival-ecommerce-website`

3. **Configure Service**
   ```
   Name: festival-ecommerce
   Runtime: Python 3
   Build Command: ./build.sh
   Start Command: gunicorn festival_ecommerce.wsgi:application
   ```

4. **Add Environment Variables**
   Click "Advanced" and add:
   ```
   SECRET_KEY = (click "Generate" button)
   DEBUG = False
   ALLOWED_HOSTS = festival-ecommerce.onrender.com
   CSRF_TRUSTED_ORIGINS = https://festival-ecommerce.onrender.com
   ```

5. **Add PostgreSQL Database**
   - Scroll down, click "Add PostgreSQL"
   - Render auto-adds DATABASE_URL

6. **Deploy!**
   - Click "Create Web Service"
   - Wait 5-10 minutes
   - **Your link:** `https://festival-ecommerce-xyz.onrender.com` 🎉

---

### Option 2: Railway.app

1. Visit https://railway.app
2. Click "Start a New Project"
3. Choose "Deploy from GitHub repo"
4. Select `AkashManda854/Capstone-Project`
5. Railway auto-detects and deploys!
6. Add environment variables in dashboard
7. **Your link:** `your-project.up.railway.app` 🎉

---

### Option 3: Heroku

1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create festival-ecommerce`
4. Add PostgreSQL: `heroku addons:create heroku-postgresql:mini`
5. Set environment variables:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   ```
6. Deploy:
   ```bash
   git push heroku copilot/build-festival-ecommerce-website:main
   ```
7. Run setup:
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py populate_data
   ```
8. **Your link:** `https://festival-ecommerce.herokuapp.com` 🎉

---

## After Deployment

### Access Your Site

Once deployed, your Festival E-Commerce website will be live at your deployment URL!

**Default Login Credentials:**
- Admin: `admin` / `admin123`
- Test User: `testuser` / `test123`

### What's Included

Your deployment includes:
- ✅ 4 Festivals (Dussehra, Diwali, Holi, Christmas)
- ✅ 5 Product Categories
- ✅ 8 Sample Products
- ✅ 2 Active Coupons (DUSSEHRA25, FESTIVE50)
- ✅ Fully functional shopping cart
- ✅ Order tracking system
- ✅ Admin dashboard at `/admin/`
- ✅ REST API at `/api/`

---

## Update README with Your Link

After deployment, update the README.md:

```markdown
## 🌐 Live Demo

**Live Link:** https://your-app-name.onrender.com

Try it now! Use credentials: `testuser` / `test123`
```

---

## Troubleshooting

### Build Failed?
- Check logs in your deployment platform
- Ensure all files are committed
- Verify `build.sh` has execute permissions

### Site Not Loading?
- Check `ALLOWED_HOSTS` includes your domain
- Verify `CSRF_TRUSTED_ORIGINS` is set
- Check application logs for errors

### Database Error?
- Ensure PostgreSQL database is connected
- Check `DATABASE_URL` environment variable
- Run migrations manually if needed

### Static Files Missing?
- Verify `collectstatic` ran during build
- Check WhiteNoise is in MIDDLEWARE
- Ensure `STATIC_ROOT` is set correctly

---

## Need Help?

1. Check deployment platform logs
2. Review [DEPLOYMENT.md](DEPLOYMENT.md) for detailed guides
3. See [QUICK_DEPLOY.md](QUICK_DEPLOY.md) for step-by-step instructions
4. Open an issue on GitHub with error details

---

## 🎉 Congratulations!

Your Festival E-Commerce website is now live and accessible to the world!

**Share your deployment link:**
- With friends and family
- On social media
- In your portfolio
- On your resume

**Next Steps:**
- Customize products in admin panel
- Add your own festivals
- Upload product images
- Configure email notifications
- Set up custom domain (optional)

---

**Ready to Deploy?** Start with Render.com - it's the easiest! 🚀

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/AkashManda854/Capstone-Project)
