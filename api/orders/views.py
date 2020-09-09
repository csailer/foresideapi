from rest_framework import viewsets
from orders import models
from . import serializers
from . import policy


class OrderViewset(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = (policy.OrderAccessPolicy,)


class OrderStatusViewset(viewsets.ModelViewSet):
    queryset = models.OrderStatus.objects.all()
    serializer_class = serializers.OrderStatusSerializer

