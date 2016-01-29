from django.db import models
from django.utils.translation import ugettext as _

from utils.choices import STATUS_CHOICES

class ResumeTemplate(models.Model):
    """
    Class representing a Resume template.
    """

    name = models.CharField(_('Name'), max_length=60, null=False, blank=False,
                            unique=True)

    code = models.CharField(_('Code'), max_length=30, null=False, blank=False,
                            unique=True)

    display_pic = models.ImageField(_('Display Picture'), null=False,
                                    blank=False)

    description = models.TextField(_('Description'), null=True, blank=False)

    status = models.CharField(_('Status'), max_length=1, null=False,
                              blank=False, choices= STATUS_CHOICES)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'rm_resume_templates'
        verbose_name_plural = 'Resume Templates'
