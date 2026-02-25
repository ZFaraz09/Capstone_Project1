# Deployment Guide - Festival E-Commerce Website

This guide covers deploying the Festival E-Commerce website to various platforms.

## Prerequisites

- Git installed
- Python 3.8+ installed
- Account on deployment platform (Heroku, AWS, DigitalOcean, etc.)

## Local Development Deployment

Already covered in the main README.md. Quick recap:

```bash
git clone https://github.com/AkashManda854/Capstone-Project.git
cd Capstone-Project
pip install -r requirements.txt
python manage.py migrate
python manage.py populate_data
python manage.py runserver
```

## Production Deployment Options

### Option 1: Heroku Deployment

#### Step 1: Prepare Your Project

1. **Install additional dependencies**
```bash
pip install gunicorn dj-database-url whitenoise psycopg2-binary
pip freeze > requirements.txt
```

2. **Create Procfile**
```bash
echo "web: gunicorn festival_ecommerce.wsgi --log-file -" > Procfile
```

3. **Create runtime.txt**
```bash
echo "python-3.12.3" > runtime.txt
```

4. **Update settings.py for production**

Add to the top of settings.py:
```python
import os
import dj_database_url

# Production settings
if 'DYNO' in os.environ:  # Running on Heroku
    DEBUG = False
    ALLOWED_HOSTS = ['your-app-name.herokuapp.com', '.herokuapp.com']
    
    # Database
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    
    # Static files
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    # Security
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
```

#### Step 2: Deploy to Heroku

```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create festival-ecommerce-app

# Add PostgreSQL database
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set DJANGO_SECRET_KEY='your-secret-key-here'
heroku config:set DEBUG=False

# Deploy
git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# Populate sample data
heroku run python manage.py populate_data

# Open your app
heroku open
```

#### Step 3: Configure Media Files (Optional)

For production, use AWS S3 for media files:

```bash
pip install boto3 django-storages
```

Add to settings.py:
```python
if 'AWS_ACCESS_KEY_ID' in os.environ:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'us-east-1'
```

### Option 2: AWS EC2 Deployment

#### Step 1: Launch EC2 Instance

1. Launch Ubuntu 22.04 LTS instance
2. Configure security group (allow ports 22, 80, 443)
3. Connect via SSH

#### Step 2: Server Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3-pip python3-venv nginx postgresql postgresql-contrib -y

# Clone repository
git clone https://github.com/AkashManda854/Capstone-Project.git
cd Capstone-Project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn psycopg2-binary
```

#### Step 3: Configure PostgreSQL

```bash
sudo -u postgres psql

CREATE DATABASE festival_ecommerce;
CREATE USER festival_user WITH PASSWORD 'your_password';
ALTER ROLE festival_user SET client_encoding TO 'utf8';
ALTER ROLE festival_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE festival_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE festival_ecommerce TO festival_user;
\q
```

Update settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'festival_ecommerce',
        'USER': 'festival_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### Step 4: Configure Gunicorn

Create `/etc/systemd/system/gunicorn.service`:

```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Capstone-Project
ExecStart=/home/ubuntu/Capstone-Project/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/home/ubuntu/Capstone-Project/festival_ecommerce.sock \
          festival_ecommerce.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start Gunicorn:
```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

#### Step 5: Configure Nginx

Create `/etc/nginx/sites-available/festival_ecommerce`:

```nginx
server {
    listen 80;
    server_name your_domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/ubuntu/Capstone-Project;
    }

    location /media/ {
        root /home/ubuntu/Capstone-Project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/Capstone-Project/festival_ecommerce.sock;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/festival_ecommerce /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 6: SSL with Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your_domain.com
```

#### Step 7: Final Steps

```bash
# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Populate data
python manage.py populate_data
```

### Option 3: DigitalOcean App Platform

1. **Connect GitHub repository**
   - Go to DigitalOcean App Platform
   - Click "Create App"
   - Connect your GitHub repository

2. **Configure App**
   - Buildpack: Python
   - Run Command: `gunicorn festival_ecommerce.wsgi:application`
   - HTTP Port: 8080

3. **Add Database**
   - Add PostgreSQL database component
   - Note connection details

4. **Set Environment Variables**
   ```
   DEBUG=False
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgresql://...
   ALLOWED_HOSTS=your-app.ondigitalocean.app
   ```

5. **Deploy**
   - Click "Deploy"
   - Wait for build to complete
   - Run migrations via console

### Option 4: Docker Deployment

#### Create Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "festival_ecommerce.wsgi:application"]
```

#### Create docker-compose.yml

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=festival_ecommerce
      - POSTGRES_USER=festival_user
      - POSTGRES_PASSWORD=festival_pass

  web:
    build: .
    command: gunicorn festival_ecommerce.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - DATABASE_URL=postgresql://festival_user:festival_pass@db:5432/festival_ecommerce
    depends_on:
      - db

  nginx:
    image: nginx:latest
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    ports:
      - "80:80"
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

#### Deploy with Docker

```bash
# Build and run
docker-compose up -d

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Populate data
docker-compose exec web python manage.py populate_data
```

## Post-Deployment Checklist

- [ ] Update `ALLOWED_HOSTS` in settings.py
- [ ] Set `DEBUG = False` in production
- [ ] Configure environment variables
- [ ] Set up database backups
- [ ] Configure SSL/HTTPS
- [ ] Set up monitoring (Sentry, New Relic)
- [ ] Configure email settings (for order confirmations)
- [ ] Set up CDN for static files (CloudFlare, AWS CloudFront)
- [ ] Configure media file storage (AWS S3)
- [ ] Set up cron jobs for periodic tasks
- [ ] Test all features in production
- [ ] Monitor logs for errors

## Environment Variables

Create a `.env` file for local development:

```bash
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1

# Email settings (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# AWS S3 settings (optional)
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
```

## Monitoring & Maintenance

### Log Monitoring

```bash
# Heroku
heroku logs --tail

# EC2
sudo journalctl -u gunicorn -f
sudo tail -f /var/log/nginx/error.log

# Docker
docker-compose logs -f web
```

### Database Backups

```bash
# PostgreSQL backup
pg_dump festival_ecommerce > backup_$(date +%Y%m%d).sql

# Restore
psql festival_ecommerce < backup_20240101.sql
```

### Scaling

For high traffic:
- Use load balancer (AWS ELB, Nginx)
- Add more Gunicorn workers
- Use caching (Redis, Memcached)
- Implement CDN
- Database read replicas
- Horizontal scaling (multiple instances)

## Troubleshooting

### Common Issues

1. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_ROOT and STATIC_URL settings
   - Verify nginx/web server configuration

2. **Database connection errors**
   - Verify DATABASE_URL
   - Check database credentials
   - Ensure database is running

3. **502 Bad Gateway**
   - Check Gunicorn is running
   - Verify socket file permissions
   - Check nginx error logs

4. **CSRF errors**
   - Add domain to CSRF_TRUSTED_ORIGINS
   - Verify CSRF_COOKIE_SECURE settings

## Performance Optimization

1. **Enable Caching**
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

2. **Database Optimization**
   - Add indexes to frequently queried fields
   - Use select_related and prefetch_related
   - Enable query caching

3. **Static File Optimization**
   - Minify CSS and JS
   - Enable gzip compression
   - Use CDN

## Support

For issues or questions:
- GitHub Issues: https://github.com/AkashManda854/Capstone-Project/issues
- Email: support@festival-ecommerce.com

---

**Happy Deploying! 🚀**
