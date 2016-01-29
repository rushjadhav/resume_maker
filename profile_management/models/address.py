from django.db import models
from django.utils.translation import ugettext as _

from utils.choices import STATUS_CHOICES

class Address(models.Model):
    """
    Class representing an address.
    """

    address1 = models.CharField(_('Address1'), max_length=40, null=False,
                                blank=False)

    address2 = models.CharField(_('Address2'), max_length=40, null=True,
                                blank=True)

    address3 = models.CharField(_('Address3'), max_length=40, null=True,
                                blank=True)

    status = models.CharField(_('Status'), max_length=1, null=False,
                              blank=False, choices= STATUS_CHOICES)

    def __unicode__(self):
        return "%s %s" %(self.address1, self.address2)

    class Meta:
        db_table = 'pm_address'
        verbose_name_plural = 'Addresses'
