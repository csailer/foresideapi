from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.contrib.auth.models import Group, User


class Command(BaseCommand):
    help = _('Creates Roles for the API.')

    def handle(self, *args, **options):
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
