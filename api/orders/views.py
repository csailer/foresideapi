from rest_framework import viewsets
from orders import models
from . import serializers
from . import policy


class OrderViewset(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = (policy.OrderAccessPolicy,)
    http_method_names = ['get', 'post', 'patch']


class OrderStatusViewset(viewsets.ModelViewSet):
    queryset = models.OrderStatus.objects.all()
    serializer_class = serializers.OrderStatusSerializer
    permission_classes = (policy.OrderStatusAccessPolicy,)
    http_method_names = ['get', 'post', 'patch']
