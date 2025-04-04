from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Avoid unnecessary query on swagger docs
        if getattr(self, 'swagger_fake_view', False):
            return Order.objects.none()

        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(buyer=user)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

    @swagger_auto_schema(
        operation_summary="Update order status (for sellers only)",
        operation_description="Allows sellers to update the status of their own orders.",
    )
    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def update_status(self, request, pk=None):
        order = self.get_object()
        user = request.user
        new_status = request.data.get('status')

        # Validation checks
        if not new_status:
            return Response({"error": "Status is required"}, status=status.HTTP_400_BAD_REQUEST)

        if new_status not in ['pending', 'in_progress', 'completed']:
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

        if not order.service or order.service.seller != user:
            return Response({"error": "You are not authorized to update this order."}, status=status.HTTP_403_FORBIDDEN)

        if order.status == new_status:
            return Response({"error": "Order is already in this status."}, status=status.HTTP_400_BAD_REQUEST)

        # Save updated status
        order.status = new_status
        order.save()

        return Response({"message": "Order status updated successfully"}, status=status.HTTP_200_OK)
