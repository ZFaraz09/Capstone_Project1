from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from shop.models import Product, Category, Festival, Order, Coupon
from accounts.models import User
from .serializers import (
    ProductSerializer, CategorySerializer, FestivalSerializer,
    OrderSerializer, CouponSerializer, UserSerializer, UserRegistrationSerializer
)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """User registration API"""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """User login API"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        })
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """Get user profile"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    """Product CRUD API"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured products"""
        products = Product.objects.filter(is_featured=True)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def trending(self, request):
        """Get trending products"""
        products = Product.objects.filter(is_trending=True)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        """Search products"""
        query = request.query_params.get('q', '')
        products = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Category API"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class FestivalViewSet(viewsets.ReadOnlyModelViewSet):
    """Festival API"""
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get active festival"""
        from datetime import date
        festival = Festival.objects.filter(
            is_active=True,
            start_date__lte=date.today(),
            end_date__gte=date.today()
        ).first()
        if festival:
            serializer = self.get_serializer(festival)
            return Response(serializer.data)
        return Response({'message': 'No active festival'}, status=status.HTTP_404_NOT_FOUND)

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    """Order API"""
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class CouponViewSet(viewsets.ReadOnlyModelViewSet):
    """Coupon API"""
    queryset = Coupon.objects.filter(is_active=True)
    serializer_class = CouponSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['post'])
    def validate(self, request):
        """Validate coupon code"""
        code = request.data.get('code')
        try:
            from datetime import date
            coupon = Coupon.objects.get(
                code=code,
                is_active=True,
                valid_from__lte=date.today(),
                valid_to__gte=date.today()
            )
            if coupon.times_used < coupon.usage_limit:
                serializer = self.get_serializer(coupon)
                return Response(serializer.data)
            return Response({'error': 'Coupon usage limit reached'}, status=status.HTTP_400_BAD_REQUEST)
        except Coupon.DoesNotExist:
            return Response({'error': 'Invalid coupon code'}, status=status.HTTP_404_NOT_FOUND)

