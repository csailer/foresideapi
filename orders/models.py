from django.db import models
from django.utils.translation import ugettext as _
import logging
from utils.models import AuditableModel

logger = logging.getLogger(__name__)


class Order(AuditableModel):

    symbol = models.CharField(verbose_name=_('Stock Symbol'), max_length=50, null=True, blank=False)
    quantity = models.IntegerField(verbose_name=_('Quantity'), null=True, blank=False)
    price = models.DecimalField(verbose_name=_('Price'), null=True, blank=False, max_digits=1000, decimal_places=8)

    def __str__(self):

        try:
            return "{0}-{1}".format(self.id, self.name)
        except:
            # whatever error happens, log warning and return an empty string
            logger.warning(_("Error occurred in __str__. Log and continue"))
            return ""

class OrderStatus(AuditableModel):

    NEW = 'new'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    STATUS_CHOICES = (
        (NEW, _('New Order')),
        (ACCEPTED, _('Accepted')),
        (REJECTED, _('Rejected'))
    )

    order = models.ForeignKey('Order', on_delete=models.CASCADE)

    status = models.CharField(verbose_name=_('Order Status'), max_length=10, null=True,
                              blank=False, choices=STATUS_CHOICES, default=NEW)
    reason = models.CharField(verbose_name=_('Reason'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.status
