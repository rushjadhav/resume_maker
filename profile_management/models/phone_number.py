from django.db import models
from django.utils.translation import ugettext as _

from phonenumber_field.modelfields import PhoneNumberField

from utils.choices import STATUS_CHOICES

class PhoneNumber(models.Model):
    """
    Class representing a phone number.
    """

    phone_number = PhoneNumberField(_('Phone Number'), blank=False, null=False,
                                    unique=True)

    status = models.CharField(_('Status'), max_length=1, null=False,
                              blank=False, choices= STATUS_CHOICES)

    def __unicode__(self):
        return self.phone_number

    class Meta:
        db_table = 'pm_phone_number'
        verbose_name_plural = 'Phone Numbers'
