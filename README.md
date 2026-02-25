# Festival-Based E-Commerce Website

A modern, responsive Django-based e-commerce platform designed for celebrating Indian festivals with dynamic festival themes, product management, and comprehensive shopping features.

## 🌐 Live Deployment

**🚀 Get Your Live Link:** See [QUICK_DEPLOY.md](QUICK_DEPLOY.md) for step-by-step deployment instructions to Render.com (FREE)

**Live Demo Link:** [Deploy your own in 10 minutes!](QUICK_DEPLOY.md)

> **Note:** To get your own live deployment link, follow the simple guide in `QUICK_DEPLOY.md`. The application is ready to deploy to Render.com, Railway.app, or PythonAnywhere with just a few clicks!

## 🎉 Features

### Core Features
- **User Authentication**: Registration, Login, and JWT/Session-based authentication
- **Festival-Based Dynamic UI**: Automatic theme switching based on active festivals
- **Product Management**: Categories, search, filters, ratings
- **Shopping Cart & Wishlist**: Full cart management with quantity updates
- **Secure Checkout**: Multiple payment methods with coupon support
- **Order Tracking**: Complete order history and status tracking
- **Admin Dashboard**: Comprehensive admin interface for managing all aspects

### Advanced Features
- Festival-based product recommendations
- Trending products highlighting
- Smart discount and coupon system
- Mobile-responsive design
- REST API endpoints for all features

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/AkashManda854/Capstone-Project.git
cd Capstone-Project
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run migrations**
```bash
python manage.py migrate
```

4. **Populate sample data**
```bash
python manage.py populate_data
```

This will create:
- Admin user: `username=admin, password=admin123`
- Test user: `username=testuser, password=test123`
- Sample festivals (Dussehra, Diwali, Holi, Christmas)
- Sample categories and products
- Sample coupons

5. **Start the development server**
```bash
python manage.py runserver
```

6. **Access the application**
- Main site: http://localhost:8000/
- Admin panel: http://localhost:8000/admin/
- API endpoints: http://localhost:8000/api/

## 📁 Project Structure

```
Capstone-Project/
├── festival_ecommerce/       # Main project settings
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── accounts/                 # User authentication app
│   ├── models.py            # Custom User model
│   └── admin.py             # User admin interface
├── shop/                     # Main shopping app
│   ├── models.py            # Product, Cart, Order models
│   ├── views.py             # Shop views and logic
│   ├── admin.py             # Shop admin interface
│   ├── urls.py              # Shop URL patterns
│   └── management/          # Custom management commands
│       └── commands/
│           └── populate_data.py  # Sample data generator
├── api/                      # REST API app
│   ├── views.py             # API views
│   ├── serializers.py       # API serializers
│   └── urls.py              # API URL patterns
├── templates/                # HTML templates
│   ├── base.html            # Base template with navbar
│   └── shop/                # Shop-specific templates
│       ├── home.html        # Dashboard/homepage
│       ├── login.html       # Login page
│       ├── register.html    # Registration page
│       ├── product_list.html    # Product listing
│       ├── product_detail.html  # Product detail page
│       ├── cart.html        # Shopping cart
│       ├── checkout.html    # Checkout page
│       ├── order_list.html  # Order history
│       ├── order_detail.html    # Order detail (invoice)
│       └── wishlist.html    # Wishlist page
├── static/                   # Static files (CSS, JS, images)
├── media/                    # User-uploaded files
└── requirements.txt          # Python dependencies
```

## 📊 Database Schema

### Main Models

#### User (Extended Django User)
- username, email, password
- phone, address, city, state, pincode
- is_admin flag

#### Festival
- name, slug, description
- start_date, end_date, is_active
- theme_color, banner_image

#### Category
- name, slug, description, image

#### Product
- name, slug, description
- price, discount_price
- category (FK), festivals (M2M)
- image, stock, rating
- is_featured, is_trending

#### Cart & CartItem
- User-specific shopping cart
- Product quantity management

#### Order & OrderItem
- order_number, status
- total_amount, discount_amount, final_amount
- shipping_address, payment_method
- Order tracking

#### Wishlist
- User's saved products

#### Coupon
- code, discount_percentage
- festival, min_purchase, max_discount
- valid_from, valid_to
- usage_limit, times_used

#### Banner
- Festival-specific banners for homepage slider

## 🔌 API Endpoints

### Authentication
- `POST /api/register/` - User registration
- `POST /api/login/` - User login (returns JWT tokens)
- `GET /api/profile/` - Get user profile (authenticated)

### Products
- `GET /api/products/` - List all products
- `GET /api/products/{id}/` - Get product details
- `GET /api/products/featured/` - Get featured products
- `GET /api/products/trending/` - Get trending products
- `GET /api/products/search/?q=query` - Search products

### Categories
- `GET /api/categories/` - List all categories
- `GET /api/categories/{id}/` - Get category details

### Festivals
- `GET /api/festivals/` - List all festivals
- `GET /api/festivals/{id}/` - Get festival details
- `GET /api/festivals/active/` - Get current active festival

### Orders
- `GET /api/orders/` - List user's orders (authenticated)
- `GET /api/orders/{id}/` - Get order details (authenticated)

### Coupons
- `GET /api/coupons/` - List active coupons
- `POST /api/coupons/validate/` - Validate coupon code

## 🎨 UI Features

### Homepage/Dashboard
- Festival-themed banner slider
- Featured products grid
- Trending products section
- Festival and category filters in navbar
- Search functionality

### Product Listing
- Advanced filters (category, festival, price, rating)
- Grid layout with product cards
- Quick add to cart
- Product images and details

### Product Detail Page
- Invoice-like detailed view
- Product specifications table
- Add to cart/wishlist buttons
- Stock information
- Related products
- Festival associations

### Shopping Cart
- Item quantity management
- Real-time price calculation
- Remove items functionality
- Order summary
- Proceed to checkout

### Checkout
- Shipping address form
- Payment method selection
- Coupon code application
- Order summary with discount calculation

### Order Tracking
- Order history list
- Detailed order view (invoice-style)
- Order status tracking timeline
- Payment and shipping details

## 👨‍💼 Admin Features

Access admin panel at `/admin/` with admin credentials.

### Manageable Entities
- **Users**: View and manage user accounts
- **Festivals**: Create/edit festivals with themes
- **Categories**: Manage product categories
- **Products**: CRUD operations, stock management
- **Banners**: Upload and manage homepage banners
- **Coupons**: Create and manage discount coupons
- **Orders**: View and update order status
- **Carts**: View user carts
- **Wishlists**: View user wishlists

## 🎯 Festival System

The platform supports dynamic festival switching:

1. **Active Festival Detection**: Automatically detects the current festival based on date
2. **Theme Switching**: Changes primary color and branding based on festival
3. **Product Filtering**: Shows festival-specific products
4. **Banner Display**: Shows relevant festival banners
5. **Coupon Association**: Links coupons to specific festivals

### Supported Festivals (Sample Data)
- Dussehra (Currently Active)
- Diwali
- Holi
- Christmas
- Sankranti, Ugadi, Eid (can be added via admin)

## 🔐 Security Features

- Password hashing with Django's built-in security
- JWT token-based API authentication
- CSRF protection on all forms
- Session-based authentication for web interface
- Secure password validation
- User role management (User/Admin)

## 📱 Responsive Design

- Mobile-first approach
- Tablet and desktop optimized
- Flexible grid layouts
- Touch-friendly interfaces
- Adaptive navigation

## 🛠️ Technologies Used

- **Backend**: Django 4.2.7, Python 3.12
- **API**: Django REST Framework 3.14.0
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Database**: SQLite (development), supports PostgreSQL/MySQL
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Icons**: Font Awesome 6.4.0
- **Image Handling**: Pillow

## 📝 Usage Guide

### For Users

1. **Registration**: Click "Register" in navbar, fill the form
2. **Login**: Use credentials to login
3. **Browse Products**: 
   - Use search bar for specific products
   - Filter by festival using dropdown
   - Filter by category
4. **View Product Details**: Click on any product card
5. **Add to Cart**: Click "Add to Cart" button
6. **Manage Cart**: View cart, update quantities, or remove items
7. **Checkout**: 
   - Enter shipping address
   - Select payment method
   - Apply coupon code if available
   - Place order
8. **Track Orders**: View order history and detailed invoices

### For Admins

1. **Login to Admin**: Go to `/admin/` and use admin credentials
2. **Manage Festivals**:
   - Add new festivals with start/end dates
   - Set theme colors
   - Mark festival as active
3. **Add Products**:
   - Fill product details
   - Upload images
   - Associate with festivals and categories
   - Set featured/trending flags
4. **Create Coupons**:
   - Set discount percentage
   - Link to specific festival
   - Set validity period and usage limits
5. **Manage Orders**:
   - Update order status
   - View order details

## 🚢 Deployment Guide

### Local Development
Already covered in Quick Start section.

### Production Deployment

#### Using Heroku

1. **Install Heroku CLI and login**
```bash
heroku login
```

2. **Create Heroku app**
```bash
heroku create your-app-name
```

3. **Add PostgreSQL**
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. **Update settings for production**
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

ALLOWED_HOSTS = ['your-app-name.herokuapp.com']
DEBUG = False
```

5. **Create Procfile**
```
web: gunicorn festival_ecommerce.wsgi
```

6. **Deploy**
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py populate_data
```

#### Using AWS/DigitalOcean

1. Set up a Ubuntu server
2. Install Python, pip, and nginx
3. Clone repository
4. Install dependencies
5. Configure Gunicorn and nginx
6. Set up SSL with Let's Encrypt
7. Use PostgreSQL for database

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👥 Team

- Developer: AkashManda854
- Project: Capstone Project - Festival E-Commerce Platform

## 📧 Support

For issues and questions, please create an issue in the GitHub repository.

## 🎓 Educational Purpose

This project was created as a capstone project to demonstrate:
- Full-stack web development with Django
- RESTful API design
- Database modeling and relationships
- User authentication and authorization
- E-commerce functionality
- Responsive web design
- Admin panel customization

---

**Happy Festival Shopping! 🎉🛍️**
