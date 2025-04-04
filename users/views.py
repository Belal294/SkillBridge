from rest_framework import status, generics, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .serializers import CustomUserSerializer, LoginSerializer
from orders.serializers import OrderSerializer
from orders.models import Order
from reviews.models import Review
from services.models import Service

User = get_user_model()


# Manage all users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


#  Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]


# Login View with JWT
class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "email": user.email,
                }
            })

        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)


# Email Verification
class VerifyEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        token = request.GET.get('token')
        if not token:
            return Response({"error": "Token not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            access_token = AccessToken(token)
            user = get_object_or_404(User, id=access_token['user_id'])
            user.is_verified = True
            user.is_active = True
            user.save()
            return Response({"message": "Email verified successfully"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


# Buyer Dashboard 
class BuyerDashboard(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.select_related('service').filter(buyer=request.user).values(
            'service__title', 'status', 'order_date'
        )
        reviews = Review.objects.select_related('service').filter(buyer=request.user).values(
            'service__title', 'rating', 'comment', 'created_at'
        )

        return Response({
            'order_history': list(orders),
            'reviews': list(reviews),
        })


# Seller Dashboard
class SellerDashboard(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        services = Service.objects.select_related('category').filter(seller=request.user).values(
            'title', 'price', 'category__name'
        )
        orders = Order.objects.select_related('buyer').filter(service__seller=request.user).values(
            'buyer__email', 'status', 'order_date'
        )
        reviews = Review.objects.select_related('buyer').filter(service__seller=request.user).values(
            'buyer__email', 'rating', 'comment', 'created_at'
        )

        return Response({
            'posted_services': list(services),
            'order_history': list(orders),
            'reviews': list(reviews),
        })
