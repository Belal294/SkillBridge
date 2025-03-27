from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model,authenticate
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from .serializers import CustomUserSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import CustomUserSerializer, LoginSerializer
from orders.serializers import OrderSerializer
from orders.models import Order
from reviews.models import Review
from services.models import Service
from rest_framework import viewsets



User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]  


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]



User = get_user_model()
class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class =  LoginSerializer

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
        return Response({"error": "Invalid Credentials"}, status=400)




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
        except:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)





class BuyerDashboard(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
     
        orders = Order.objects.filter(buyer=request.user).values('service__title', 'status', 'order_date')
        
        reviews = Review.objects.filter(buyer=request.user).values('service__title', 'rating', 'comment', 'created_at')

        data = {
            'order_history': list(orders),
            'reviews': list(reviews),
        }
        
        return Response(data)
    





class SellerDashboard(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        services = Service.objects.filter(seller=request.user).values('title', 'price', 'category__name')

        orders = Order.objects.filter(service__seller=request.user).values('buyer__email', 'status', 'order_date')

        reviews = Review.objects.filter(service__seller=request.user).values('buyer__email', 'rating', 'comment', 'created_at')

        data = {
            'posted_services': list(services),
            'order_history': list(orders),
            'reviews': list(reviews),
        }
        
        return Response(data)