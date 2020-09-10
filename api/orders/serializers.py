from rest_framework import serializers
from orders import models


class OrderStatusSerializer(serializers.ModelSerializer):
    modified_by = serializers.CharField(required=False)

    class Meta:
        model = models.OrderStatus
        fields = ('id', 'order', 'status', 'reason', 'modified_by')


class OrderSerializer(serializers.ModelSerializer):
    status = OrderStatusSerializer(required=False, many=True, read_only=False)
    created_by = serializers.CharField(required=False)
    order_time = serializers.DateTimeField(required=False, source='create_date')

    class Meta:
        model = models.Order
        fields = ('id',
                  'name',
                  'client',
                  'symbol',
                  'quantity',
                  'price',
                  'transaction_type',
                  'payment_method',
                  'created_by',
                  'order_time',
                  'status')

    def create(self, validated_data):
        '''
         Called when an order is created
        '''

        # Create/Save the order
        order = models.Order.objects.create(**validated_data)

        # this is a new order so set the 'new' status
        models.OrderStatus.objects.create(
            order=order,
            status=models.OrderStatus.NEW,
            reason='new order'
        )

        return order
