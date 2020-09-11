from rest_framework import serializers
from orders import models
from cuser.middleware import CuserMiddleware


class OrderStatusSerializer(serializers.ModelSerializer):
    modified_by = serializers.CharField(required=False)
    created_by = serializers.CharField(required=False)
    create_date = serializers.DateTimeField(required=False)
    modified_date = serializers.DateTimeField(required=False)
    modified_by = serializers.CharField(required=False)

    class Meta:
        model = models.OrderStatus
        fields = ('id',
                  'order',
                  'status',
                  'reason',
                  'created_by',
                  'create_date',
                  'modified_by',
                  'modified_date')

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request is not None: CuserMiddleware.set_user(request.user)
        return super(OrderStatusSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request is not None: CuserMiddleware.set_user(request.user)
        return super(OrderStatusSerializer, self).update(instance, validated_data)


class OrderSerializer(serializers.ModelSerializer):
    status = OrderStatusSerializer(required=False, many=True, read_only=False)
    created_by = serializers.CharField(required=False)
    modified_date = serializers.DateTimeField(required=False)
    modified_by = serializers.CharField(required=False)
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
                  'modified_by',
                  'modified_date',
                  'status')

    def create(self, validated_data):
        '''
         Called when an order is created
        '''
        request = self.context.get('request', None)
        if request is not None: CuserMiddleware.set_user(request.user)

        # Create/Save the order
        order = models.Order.objects.create(**validated_data)

        # this is a new order so set the 'new' status
        models.OrderStatus.objects.create(
            order=order,
            status=models.OrderStatus.NEW,
            reason='new order'
        )

        return order

    def partial_update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request is not None: CuserMiddleware.set_user(request.user)
        return super(OrderSerializer, self).partial_update(instance, validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request is not None: CuserMiddleware.set_user(request.user)
        return super(OrderSerializer, self).update(instance, validated_data)
