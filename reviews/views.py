from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Review
from .serializers import ReviewSerializer
from orders.models import Order
from rest_framework import status
from rest_framework.exceptions import NotFound

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        order_id = self.request.data.get('order') 
        print(f"Order ID: {order_id}")
        
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            raise NotFound({"error": "Order not found."})  
        
        if order.buyer == self.request.user and order.status == 'completed':  
            serializer.save(buyer=self.request.user, service=order.service, order=order)
        else:
            return Response({"error": "You can only review after completing the order."}, status=status.HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        if not self.request.user or self.request.user.is_anonymous:
            return Review.objects.none() 

        return Review.objects.filter(service__seller=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_reviews(self, request):
        reviews = Review.objects.filter(buyer=request.user)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)
