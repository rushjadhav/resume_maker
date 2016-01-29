from django.db import models
from django.utils.translation import ugettext as _

from utils.choices import STATUS_CHOICES
from profile_management.models import Email, PhoneNumber, Address

class Institude(models.Model):
    """
    Class representing an institude.
    """

    name = models.CharField(_('Name'), max_length=120, null=False, blank=False,
                            unique=True)

    date_of_establishment = models.DateField(_('Date of Establishment'),
                                            null=True, blank=True)

    email = models.ForeignKey(Email, null=True, blank=True,
                              related_name='email_institudes')

    phone_number = models.ForeignKey(PhoneNumber, null=True, blank=True,
                                     related_name='phone_number_institudes')

    address = models.ForeignKey(Address, null=True, blank=True,
                                related_name='address_institudes')

    status = models.CharField(_('Status'), max_length=1, null=False,
                              blank=False, choices= STATUS_CHOICES)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'edum_institude'
        verbose_name_plural = 'Institudes'
