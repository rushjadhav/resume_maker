from django.db import models
from django.utils.translation import ugettext as _

from utils.choices import STATUS_CHOICES

class Hobby(models.Model):
    """
    Class representing a Hobby. e.g: swimming, dancing etc.
    """

    name = models.CharField(_('Name'), max_length=120, null=False, blank=False,
                            unique=True)

    status = models.CharField(_('Status'), max_length=1, null=False,
                              blank=False, choices= STATUS_CHOICES)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'pm_hobby'
        verbose_name_plural = 'Hobbies'
