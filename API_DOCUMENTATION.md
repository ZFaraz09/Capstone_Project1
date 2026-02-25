# API Documentation

## Base URL
```
http://localhost:8000/api/
```

## Authentication

The API uses JWT (JSON Web Token) for authentication. After registration or login, you'll receive an access token and a refresh token.

### Register
**Endpoint:** `POST /api/register/`

**Request Body:**
```json
{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "9876543210"
}
```

**Response:**
```json
{
    "user": {
        "id": 1,
        "username": "johndoe",
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "phone": "9876543210"
    },
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
}
```

### Login
**Endpoint:** `POST /api/login/`

**Request Body:**
```json
{
    "username": "johndoe",
    "password": "securepassword123"
}
```

**Response:**
```json
{
    "user": {
        "id": 1,
        "username": "johndoe",
        "email": "john@example.com"
    },
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
}
```

### Get User Profile
**Endpoint:** `GET /api/profile/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
{
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "9876543210",
    "address": "123 Main St",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400001"
}
```

## Products

### List All Products
**Endpoint:** `GET /api/products/`

**Response:**
```json
[
    {
        "id": 1,
        "name": "Traditional Silk Saree",
        "slug": "traditional-silk-saree",
        "description": "Beautiful handwoven silk saree...",
        "price": "5999.00",
        "discount_price": "4499.00",
        "category": 1,
        "category_name": "Clothing",
        "festivals": [1, 2],
        "festivals_data": [
            {
                "id": 1,
                "name": "Dussehra",
                "slug": "dussehra"
            }
        ],
        "image": "/media/products/saree.jpg",
        "stock": 50,
        "rating": "4.50",
        "is_featured": true,
        "is_trending": true
    }
]
```

### Get Product Detail
**Endpoint:** `GET /api/products/{id}/`

**Response:**
```json
{
    "id": 1,
    "name": "Traditional Silk Saree",
    "slug": "traditional-silk-saree",
    "description": "Beautiful handwoven silk saree perfect for festival celebrations.",
    "price": "5999.00",
    "discount_price": "4499.00",
    "category": 1,
    "category_name": "Clothing",
    "festivals": [1, 2],
    "image": "/media/products/saree.jpg",
    "stock": 50,
    "rating": "4.50",
    "is_featured": true,
    "is_trending": true
}
```

### Get Featured Products
**Endpoint:** `GET /api/products/featured/`

Returns products marked as featured.

### Get Trending Products
**Endpoint:** `GET /api/products/trending/`

Returns products marked as trending.

### Search Products
**Endpoint:** `GET /api/products/search/?q=saree`

**Query Parameters:**
- `q`: Search query

**Response:** Array of products matching the search query

## Categories

### List All Categories
**Endpoint:** `GET /api/categories/`

**Response:**
```json
[
    {
        "id": 1,
        "name": "Clothing",
        "slug": "clothing",
        "description": "Traditional and modern clothing",
        "image": "/media/categories/clothing.jpg",
        "created_at": "2024-01-01T00:00:00Z"
    }
]
```

### Get Category Detail
**Endpoint:** `GET /api/categories/{id}/`

Returns details of a specific category.

## Festivals

### List All Festivals
**Endpoint:** `GET /api/festivals/`

**Response:**
```json
[
    {
        "id": 1,
        "name": "Dussehra",
        "slug": "dussehra",
        "description": "Celebrate the victory of good over evil...",
        "start_date": "2024-10-01",
        "end_date": "2024-10-15",
        "is_active": true,
        "theme_color": "#FF6B35",
        "banner_image": "/media/festivals/dussehra.jpg"
    }
]
```

### Get Festival Detail
**Endpoint:** `GET /api/festivals/{id}/`

Returns details of a specific festival.

### Get Active Festival
**Endpoint:** `GET /api/festivals/active/`

Returns the currently active festival based on date.

**Response:**
```json
{
    "id": 1,
    "name": "Dussehra",
    "slug": "dussehra",
    "description": "Celebrate the victory of good over evil...",
    "start_date": "2024-10-01",
    "end_date": "2024-10-15",
    "is_active": true,
    "theme_color": "#FF6B35"
}
```

## Orders

### List User Orders
**Endpoint:** `GET /api/orders/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
[
    {
        "id": 1,
        "user": 1,
        "order_number": "ORD1234567890",
        "total_amount": "10000.00",
        "discount_amount": "500.00",
        "final_amount": "9500.00",
        "coupon": 1,
        "status": "pending",
        "shipping_address": "123 Main St, Mumbai",
        "payment_method": "COD",
        "created_at": "2024-01-15T10:30:00Z",
        "items": [
            {
                "id": 1,
                "product": 1,
                "product_name": "Traditional Silk Saree",
                "quantity": 2,
                "price": "4499.00"
            }
        ]
    }
]
```

### Get Order Detail
**Endpoint:** `GET /api/orders/{id}/`

**Headers:**
```
Authorization: Bearer <access_token>
```

Returns detailed information about a specific order.

## Coupons

### List Active Coupons
**Endpoint:** `GET /api/coupons/`

**Response:**
```json
[
    {
        "id": 1,
        "code": "DUSSEHRA25",
        "discount_percentage": 25,
        "festival": 1,
        "min_purchase": "1000.00",
        "max_discount": "500.00",
        "valid_from": "2024-10-01T00:00:00Z",
        "valid_to": "2024-10-15T23:59:59Z",
        "is_active": true,
        "usage_limit": 100,
        "times_used": 25
    }
]
```

### Validate Coupon
**Endpoint:** `POST /api/coupons/validate/`

**Request Body:**
```json
{
    "code": "DUSSEHRA25"
}
```

**Response (Valid):**
```json
{
    "id": 1,
    "code": "DUSSEHRA25",
    "discount_percentage": 25,
    "min_purchase": "1000.00",
    "max_discount": "500.00"
}
```

**Response (Invalid):**
```json
{
    "error": "Invalid coupon code"
}
```

## Error Responses

All endpoints may return error responses in the following format:

### 400 Bad Request
```json
{
    "field_name": [
        "Error message for this field"
    ]
}
```

### 401 Unauthorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### 404 Not Found
```json
{
    "detail": "Not found."
}
```

### 500 Internal Server Error
```json
{
    "error": "An unexpected error occurred."
}
```

## Using the API

### Example with cURL

**Register a new user:**
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

**Get products:**
```bash
curl http://localhost:8000/api/products/
```

**Get user profile (authenticated):**
```bash
curl http://localhost:8000/api/profile/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example with Python (requests)

```python
import requests

# Register
response = requests.post('http://localhost:8000/api/register/', json={
    'username': 'johndoe',
    'email': 'john@example.com',
    'password': 'securepassword123',
    'first_name': 'John',
    'last_name': 'Doe'
})

data = response.json()
access_token = data['tokens']['access']

# Get products
response = requests.get('http://localhost:8000/api/products/')
products = response.json()

# Get user profile (authenticated)
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get('http://localhost:8000/api/profile/', headers=headers)
profile = response.json()
```

### Example with JavaScript (fetch)

```javascript
// Register
fetch('http://localhost:8000/api/register/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        username: 'johndoe',
        email: 'john@example.com',
        password: 'securepassword123',
        first_name: 'John',
        last_name: 'Doe'
    })
})
.then(response => response.json())
.then(data => {
    const accessToken = data.tokens.access;
    localStorage.setItem('access_token', accessToken);
});

// Get products
fetch('http://localhost:8000/api/products/')
.then(response => response.json())
.then(products => console.log(products));

// Get user profile (authenticated)
const accessToken = localStorage.getItem('access_token');
fetch('http://localhost:8000/api/profile/', {
    headers: {
        'Authorization': `Bearer ${accessToken}`
    }
})
.then(response => response.json())
.then(profile => console.log(profile));
```

## Rate Limiting

Currently, no rate limiting is implemented. For production, consider implementing rate limiting using packages like `django-ratelimit`.

## CORS

CORS is enabled for all origins in development. For production, update the `CORS_ALLOW_ALL_ORIGINS` setting in `settings.py` to restrict allowed origins.

## Pagination

List endpoints support pagination. By default, 30 items are returned per page.

**Query Parameters:**
- `page`: Page number (default: 1)
- `page_size`: Items per page (default: 30, max: 100)

**Example:**
```
GET /api/products/?page=2&page_size=20
```
