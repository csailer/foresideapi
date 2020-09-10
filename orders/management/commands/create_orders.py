
import datetime
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from orders import models
class Command(BaseCommand):
    help = _('Creates Fake Orders for the API.')

    def handle(self, *args, **options):

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


# name	order_time	client	stock	quantity	price	transaction_type	payment_method	settlement	status	reason	modified by
# Order1	3/28/19	Client1	AAPL	10000	50.00	create	cash	4/1/19	new	new order	trader