from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from utils.testdata import TestDataFixture


class Command(BaseCommand):
    help = _('Creates Roles for the API.')

    def handle(self, *args, **options):
       TestDataFixture().create_roles()