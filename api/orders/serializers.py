from rest_framework import serializers
from orders import models


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ('id', 'symbol', 'quantity', 'price')


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderStatus
        fields = ('id', 'order', 'status', 'reason')