from django.db import models
from django.utils.translation import ugettext as _

from utils.choices import STATUS_CHOICES
from resume_management.models import Resume

class Experience(models.Model):
    """
    Class representing an user experience.
    """

    resume = models.ForeignKey(Resume, null=False, blank=False,
                              related_name='resume_experiences')

    company = models.ForeignKey('Company', null=False, blank=False)

    from_date = models.DateField(_('From Date'), null=False, blank=False)

    to_date = models.DateField(_('To Date '), null=True, blank=True)

    designation = models.CharField(_('Designation'), max_length=40, null=False,
                                  blank=False)

    status = models.CharField(_('Status'), max_length=1, null=False,
                              blank=False, choices= STATUS_CHOICES)

    def __unicode__(self):
        return "%s (%s)" %(self.resume.name, self.company.name)

    class Meta:
        db_table = 'em_experience'
        verbose_name_plural = 'Experiences'
