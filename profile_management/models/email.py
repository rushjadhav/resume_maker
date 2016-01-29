from django.db import models
from django.utils.translation import ugettext as _

from utils.choices import STATUS_CHOICES

class Email(models.Model):
    """
    Class representing an email.
    """

    email = models.EmailField(_('Email'), null=False, blank=False, unique=True)

    status = models.CharField(_('Status'), max_length=1, null=False,
                              blank=False, choices= STATUS_CHOICES)

    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'pm_email'
        verbose_name_plural = 'Emails'
