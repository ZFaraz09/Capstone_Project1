from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Festival, Banner, Cart, CartItem, Wishlist, Order, OrderItem, Coupon
from accounts.models import User
from datetime import date
import uuid

def home(request):
    """Dashboard/Home page with festival theme"""
    active_festival = Festival.objects.filter(
        is_active=True,
        start_date__lte=date.today(),
        end_date__gte=date.today()
    ).first()
    
    banners = Banner.objects.filter(is_active=True)
    if active_festival:
        banners = banners.filter(Q(festival=active_festival) | Q(festival__isnull=True))
    
    featured_products = Product.objects.filter(is_featured=True)[:8]
    trending_products = Product.objects.filter(is_trending=True)[:8]
    
    # Filter by selected festival if provided
    selected_festival = request.GET.get('festival')
    if selected_festival:
        try:
            festival = Festival.objects.get(slug=selected_festival)
            featured_products = featured_products.filter(festivals=festival)
            trending_products = trending_products.filter(festivals=festival)
        except Festival.DoesNotExist:
            pass
    
    festivals = Festival.objects.all()
    categories = Category.objects.all()
    
    context = {
        'banners': banners,
        'featured_products': featured_products,
        'trending_products': trending_products,
        'festivals': festivals,
        'categories': categories,
        'selected_festival': selected_festival,
    }
    return render(request, 'shop/home.html', context)

def user_login(request):
    """User login page"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'shop/login.html')

def user_register(request):
    """User registration page"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        phone = request.POST.get('phone', '')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone=phone
            )
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
    
    return render(request, 'shop/register.html')

def user_logout(request):
    """User logout"""
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

def product_list(request):
    """Product listing with search and filters"""
    products = Product.objects.all()
    
    # Search
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    # Festival filter
    festival_slug = request.GET.get('festival')
    if festival_slug:
        products = products.filter(festivals__slug=festival_slug)
    
    # Price filter
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    
    # Rating filter
    min_rating = request.GET.get('rating')
    if min_rating:
        products = products.filter(rating__gte=min_rating)
    
    categories = Category.objects.all()
    festivals = Festival.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'festivals': festivals,
        'search_query': search_query,
    }
    return render(request, 'shop/product_list.html', context)

def product_detail(request, slug):
    """Product detail page"""
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'shop/product_detail.html', context)

@login_required
def cart_view(request):
    """Shopping cart page"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    context = {
        'cart': cart,
    }
    return render(request, 'shop/cart.html', context)

@login_required
def add_to_cart(request, product_id):
    """Add product to cart"""
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f'{product.name} added to cart!')
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def remove_from_cart(request, item_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('cart')

@login_required
def update_cart(request, item_id):
    """Update cart item quantity"""
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated!')
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart!')
    
    return redirect('cart')

@login_required
def wishlist_view(request):
    """Wishlist page"""
    wishlist_items = Wishlist.objects.filter(user=request.user)
    
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'shop/wishlist.html', context)

@login_required
def add_to_wishlist(request, product_id):
    """Add product to wishlist"""
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    
    if created:
        messages.success(request, f'{product.name} added to wishlist!')
    else:
        messages.info(request, f'{product.name} is already in your wishlist!')
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def remove_from_wishlist(request, wishlist_id):
    """Remove item from wishlist"""
    wishlist_item = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)
    wishlist_item.delete()
    messages.success(request, 'Item removed from wishlist!')
    return redirect('wishlist')

@login_required
def checkout(request):
    """Checkout page"""
    cart = get_object_or_404(Cart, user=request.user)
    
    if request.method == 'POST':
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method', 'COD')
        coupon_code = request.POST.get('coupon_code', '')
        
        total_amount = cart.total_price
        discount_amount = 0
        coupon = None
        
        # Apply coupon if provided
        if coupon_code:
            try:
                coupon = Coupon.objects.get(
                    code=coupon_code,
                    is_active=True,
                    valid_from__lte=date.today(),
                    valid_to__gte=date.today()
                )
                if coupon.times_used < coupon.usage_limit:
                    if total_amount >= coupon.min_purchase:
                        discount_amount = (total_amount * coupon.discount_percentage) / 100
                        if coupon.max_discount:
                            discount_amount = min(discount_amount, coupon.max_discount)
                        coupon.times_used += 1
                        coupon.save()
                    else:
                        messages.warning(request, f'Minimum purchase of ₹{coupon.min_purchase} required for this coupon')
                        coupon = None
                else:
                    messages.warning(request, 'Coupon usage limit reached')
                    coupon = None
            except Coupon.DoesNotExist:
                messages.warning(request, 'Invalid coupon code')
        
        final_amount = total_amount - discount_amount
        
        # Create order
        order = Order.objects.create(
            user=request.user,
            order_number=f'ORD{uuid.uuid4().hex[:10].upper()}',
            total_amount=total_amount,
            discount_amount=discount_amount,
            final_amount=final_amount,
            coupon=coupon,
            shipping_address=address,
            payment_method=payment_method,
            status='pending'
        )
        
        # Create order items
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.final_price
            )
        
        # Clear cart
        cart.items.all().delete()
        
        messages.success(request, f'Order placed successfully! Order number: {order.order_number}')
        return redirect('order_detail', order_id=order.id)
    
    context = {
        'cart': cart,
    }
    return render(request, 'shop/checkout.html', context)

@login_required
def order_list(request):
    """User's order list"""
    orders = Order.objects.filter(user=request.user)
    
    context = {
        'orders': orders,
    }
    return render(request, 'shop/order_list.html', context)

@login_required
def order_detail(request, order_id):
    """Order detail page"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
    }
    return render(request, 'shop/order_detail.html', context)

