from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'festivals', views.FestivalViewSet)
router.register(r'orders', views.OrderViewSet, basename='order')
router.register(r'coupons', views.CouponViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register, name='api_register'),
    path('login/', views.login, name='api_login'),
    path('profile/', views.user_profile, name='api_profile'),
]
