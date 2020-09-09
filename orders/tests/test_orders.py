from django.test import TestCase
from mixer.backend.django import mixer
from orders.models import Order, OrderStatus
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status


class OrderTest(TestCase):
    '''
    Tests for the Order Model
    '''

    def test_create_order(self):
        '''
        Tests creating an order
        :return:
        '''
        order = mixer.blend(Order, symbol='APPL', price=133.00, quantity=10)
        new_order = Order.objects.get(pk=order.pk)

        self.assertEqual(True, new_order is not None)
        self.assertTrue(new_order.symbol=='APPL')
        self.assertTrue(new_order.price == 133.00)
        self.assertTrue(new_order.quantity==10)

        with self.assertRaises(Order.DoesNotExist) as e:
            Order.objects.get(pk=2000)

    def test_order_status(self):
        '''
        Tests adding an order status
        :return:
        '''
        order = mixer.blend(Order, symbol='APPL', price=133.00, quantity=10)

        order_status = OrderStatus(
            order=order,
            status='new',
            reason='new order'
        )

        self.assertEqual(True, order_status is not None)
        self.assertTrue(order_status.order == order)
        self.assertTrue(order_status.status == 'new')
        self.assertTrue(order_status.reason == 'new order')

        with self.assertRaises(OrderStatus.DoesNotExist) as e:
            OrderStatus.objects.get(pk=2000)


    def test_delete_order(self):
        '''
        Tests deleting an order. Which should also delete the order status via a cascading delete
        :return:
        '''
        order = mixer.blend(Order, symbol='APPL', price=133.00, quantity=10)

        order_status = OrderStatus(
            order=order,
            status='new',
            reason='new order'
        )

        self.assertEqual(True, order_status is not None)
        self.assertTrue(order_status.order == order)
        self.assertTrue(order_status.status == 'new')
        self.assertTrue(order_status.reason == 'new order')

        # Delete the order
        order.delete()

        # test that the OrderStatus deleted on the cascade
        with self.assertRaises(OrderStatus.DoesNotExist) as e:
            OrderStatus.objects.get(pk=order_status.pk)

