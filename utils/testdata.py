import datetime
from django.contrib.auth.models import Group, User
from orders import models


class TestDataFixture:

    def create_roles(self):
        groups = Group.objects.all()
        groups.delete()

        trader_group = Group.objects.create(
            name='Trader'
        )

        approver_group = Group.objects.create(
            name='Approver'
        )

        admin_group = Group.objects.create(
            name='Admin'
        )

        users = User.objects.all()
        users.delete()

        trader_user = User.objects.create_user(username='jtrader', password='foreside2020')
        trader_user.first_name = 'Joe'
        trader_user.last_name = 'Trader'

        trader_user.groups.add(trader_group)
        trader_user.save()

        approver_user = User.objects.create_user(username='japprover', password='foreside2020')
        approver_user.first_name = 'Joe'
        approver_user.last_name = 'Approver'
        approver_user.is_staff = True

        approver_user.groups.add(approver_group)
        approver_user.save()

        admin_user = User.objects.create_user(username='jadmin', password='foreside2020')
        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.first_name = 'Joe'
        admin_user.last_name = 'Admin'

        admin_user.groups.add(admin_group)
        admin_user.save()

    def create_orders(self):
        trader_user = User.objects.get(username='jtrader')

        orders = models.Order.objects.all()
        orders.delete()

        order = models.Order.objects.create(
            name='Order1',
            client='Client1',
            symbol='APPL',
            quantity=10000,
            transaction_type=models.Order.CREATE,
            price=50,
            payment_method=models.Order.CASH,
            created_by=trader_user,
            create_date=datetime.datetime.utcnow(),
            modified_by=trader_user,
            modified_date=datetime.datetime.utcnow()
        )

        models.OrderStatus.objects.create(
            order=order,
            status=models.OrderStatus.NEW,
            reason='new order',
            created_by=trader_user,
            create_date=datetime.datetime.utcnow(),
            modified_by=trader_user,
            modified_date=datetime.datetime.utcnow()
        )

        order = models.Order.objects.create(
            name='Order2',
            client='Client2',
            symbol='APPL',
            quantity=10000,
            transaction_type=models.Order.CREATE,
            price=50,
            payment_method=models.Order.CASH,
            created_by=trader_user,
            create_date=datetime.datetime.utcnow(),
            modified_by=trader_user,
            modified_date=datetime.datetime.utcnow()
        )

        models.OrderStatus.objects.create(
            order=order,
            status=models.OrderStatus.NEW,
            reason='new order',
            created_by=trader_user,
            create_date=datetime.datetime.utcnow(),
            modified_by=trader_user,
            modified_date=datetime.datetime.utcnow()
        )
