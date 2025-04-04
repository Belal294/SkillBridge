from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Retrieve orders for the logged-in buyer",
        operation_description="Returns a list of orders for the authenticated user who is a buyer.",
    )
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Order.objects.none()

        if self.request.user.is_staff: 
            return Order.objects.all()

        return Order.objects.filter(buyer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def update_status(self, request, pk=None):
        try:
            order = self.get_object()
            new_status = request.data.get('status')

            if not new_status:
                return Response({"error": "Status is required"}, status=status.HTTP_400_BAD_REQUEST)

            if new_status not in ['pending', 'in_progress', 'completed']:
                return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

            if not hasattr(order, "service") or order.service is None:
                return Response({"error": "Order does not have an associated service"}, status=status.HTTP_400_BAD_REQUEST)

            if order.service.seller != request.user:
                return Response({"error": "You can only update your own orders"}, status=status.HTTP_403_FORBIDDEN)

            if order.status == new_status:
                return Response({"error": "Order is already in this status"}, status=status.HTTP_400_BAD_REQUEST)

            order.status = new_status
            order.save()

            return Response({"message": "Order status updated successfully"}, status=status.HTTP_200_OK)

        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
