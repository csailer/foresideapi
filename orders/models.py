from django.db import models
from django.utils.translation import ugettext as _
import logging
from utils.models import AuditableModel

logger = logging.getLogger(__name__)


class Order(AuditableModel):

    # TODO: Refactor in future sprint
    # These would be better moved to a data store so that
    # they can be added to and modified more easily.
    CREATE = 'create'
    REDEEM = 'redeem'
    CASH = 'cash'
    KIND = 'kind'

    TRANSACTION_TYPE_CHOICES = (
        (CREATE, _('Create')),
        (REDEEM, _('Redeem'))
    )

    PAYMENT_TYPE_CHOICES = (
        (CASH, _('Cash')),
        (KIND, _('Kind'))
    )

    # TODO: Future Sprint: Move clients to their own model/table and update the client field to a ForeignKey to the client model
    name= models.CharField(verbose_name=_('Name'), max_length=150, null=True, blank=False)
    client = models.CharField(verbose_name=_('Client'), max_length=150, null=True, blank=False)
    symbol = models.CharField(verbose_name=_('Stock Symbol'), max_length=50, null=True, blank=False)
    quantity = models.IntegerField(verbose_name=_('Quantity'), null=True, blank=False)
    price = models.DecimalField(verbose_name=_('Price'), null=True, blank=False, max_digits=1000, decimal_places=8)
    transaction_type = models.CharField(verbose_name=_('Transaction Type'), max_length=10, null=True,
                              blank=False, choices=TRANSACTION_TYPE_CHOICES, default=CREATE)
    payment_method = models.CharField(verbose_name=_('Payment Method'), max_length=10, null=True,
                                        blank=False, choices=PAYMENT_TYPE_CHOICES, default=CASH)

    def __str__(self):

        try:
            return "{0}-{1}".format(self.id, self.name)
        except:
            # whatever error happens, log warning and return an empty string
            logger.warning(_("Error occurred in __str__. Log and continue"))
            return ""

class OrderStatus(AuditableModel):

    NEW = 'new'
    APPROVED = 'approved'
    REJECTED = 'rejected'

    STATUS_CHOICES = (
        (NEW, _('New Order')),
        (APPROVED, _('Approved')),
        (REJECTED, _('Rejected'))
    )

    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='status')

    status = models.CharField(verbose_name=_('Order Status'), max_length=10, null=True,
                              blank=False, choices=STATUS_CHOICES, default=NEW)
    reason = models.CharField(verbose_name=_('Reason'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['-modified_date']