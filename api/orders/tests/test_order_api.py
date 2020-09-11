import json
from rest_framework import status
from django.test import TestCase, Client

from django.urls import reverse
from orders import models
from ..serializers import OrderSerializer, OrderStatusSerializer


# initialize the APIClient app
client = Client()
class OrderApiTest(TestCase):

    def setUp(self):
        pass

    def test_get_orders(self):
        # get API response
        response = client.get(reverse('get_orders'))
        # get data from db
        orders = models.Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
