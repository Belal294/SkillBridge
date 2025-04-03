from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Service, Category
from rest_framework.exceptions import PermissionDenied
from .serializers import ServiceSerializer, CategorySerializer, ServiceImageSerializer, ServiceImage
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadOnly
from django.shortcuts import get_object_or_404


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category']
    ordering_fields = ['price']
    search_fields = ['title', 'description']
    parser_classes = [MultiPartParser, FormParser] 
    

    def get_queryset(self):
        queryset = Service.objects.all()
        
        sort_by = self.request.query_params.get('sort', None)
        if sort_by == 'price_low_to_high':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_high_to_low':
            queryset = queryset.order_by('-price')

        return queryset

    def perform_create(self, serializer):
        if not self.request.user or self.request.user.is_anonymous:
            raise PermissionDenied("You must be logged in to create a service.")
        
        serializer.save(seller=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  


class ServiceImageViewSet(ModelViewSet):
    serializer_class = ServiceImageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return ServiceImage.objects.filter(service_id=self.kwargs.get('service_pk'))

    def perform_create(self, serializer):
        service = get_object_or_404(Service, id=self.kwargs.get('service_pk'))
        serializer.save(service=service)  


