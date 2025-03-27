from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Service, Category
from .serializers import ServiceSerializer, CategorySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category']
    ordering_fields = ['price']
    search_fields = ['title', 'description']

    def get_queryset(self):
        queryset = Service.objects.all()

        sort_by = self.request.query_params.get('sort', None)
        if sort_by == 'price_low_to_high':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_high_to_low':
            queryset = queryset.order_by('-price')

        return queryset

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
