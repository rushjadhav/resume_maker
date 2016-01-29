from django.db import models
from django.utils.translation import ugettext as _

from utils.choices import STATUS_CHOICES

class Skill(models.Model):
    """
    Class representing an skill. e.g: HTML, CSS etc.
    """

    name = models.CharField(_('Name'), max_length=120, null=False, blank=False,
                            unique=True)

    status = models.CharField(_('Status'), max_length=1, null=False,
                              default='A', blank=False, choices= STATUS_CHOICES)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'pm_skill'
        verbose_name_plural = 'Skills'
