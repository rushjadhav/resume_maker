from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from profile_management.models import Hobby

class ResumeHobbyMap(models.Model):
    """
    Class representing a mapping between resume and hobby.
    """

    resume = models.ForeignKey('Resume', null=False, blank=False,
                              related_name='resume_hobbies')

    hobby = models.ForeignKey(Hobby, null=False, blank=False)

    efficiency_level = models.IntegerField(_('Efficiency Level'), null=False,
                                        blank=False,
                                        validators=[MaxValueValidator(100),
                                                    MinValueValidator(1)])

    def __unicode__(self):
        return "%s (%s)" %(self.resume.user.username, self.hobby.name)

    class Meta:
        db_table = 'rm_resume_hobby_map'
        verbose_name_plural = 'Resume Hobbies'
        unique_together = (('resume', 'hobby'),)
