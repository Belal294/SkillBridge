from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from users.views import RegisterView, VerifyEmailView, LoginView, BuyerDashboard, SellerDashboard, UserViewSet
from services.views import ServiceViewSet, CategoryViewSet, ServiceImageViewSet
from orders.views import OrderViewSet
from notifications.views import NotificationViewSet
from dashboard.views import AdminDashboardView
from reviews.views import ReviewViewSet

# 🔹 Parent Router
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('services', ServiceViewSet, basename='services')
router.register('categories', CategoryViewSet, basename='category')
router.register('orders', OrderViewSet, basename='order')
router.register('notifications', NotificationViewSet, basename='notification')
router.register('reviews', ReviewViewSet, basename='review')

# 🔹 Nested Router for Service Images
services_router = NestedDefaultRouter(router, 'services', lookup='service')
services_router.register('images', ServiceImageViewSet, basename='service-images')

urlpatterns = [
    path('', include(router.urls)), 
    path('', include(services_router.urls)),  
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('orders/<int:pk>/update-status/', OrderViewSet.as_view({'patch': 'update_status'}), name='update-status'),
    path('buyer-dashboard/', BuyerDashboard.as_view(), name='buyer_dashboard'),
    path('seller-dashboard/', SellerDashboard.as_view(), name='seller_dashboard'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
