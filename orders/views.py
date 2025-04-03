from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import PermissionDenied
from .models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer
from rest_framework.decorators import action

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to view orders.")
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(buyer=self.request.user)

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to create an order.")
        serializer.save(buyer=self.request.user)

    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def update_status(self, request, pk=None):
        try:
            if not request.user.is_authenticated:
                raise PermissionDenied("You must be logged in to update an order status.")
            
            order = self.get_object()
            new_status = request.data.get('status')

            if new_status not in ['pending', 'in_progress', 'completed']:
                return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

            if order.service.seller != request.user:
                return Response({"error": "You can only update your own orders"}, status=status.HTTP_403_FORBIDDEN)

            order.status = new_status
            order.save()

            return Response({"message": "Order status updated successfully"}, status=status.HTTP_200_OK)

        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
