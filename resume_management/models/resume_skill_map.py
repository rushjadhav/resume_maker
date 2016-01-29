from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from profile_management.models import Skill

class ResumeSkillMap(models.Model):
    """
    Class representing a mapping between resume and skill.
    """

    resume = models.ForeignKey('Resume', null=False, blank=False,
                               related_name='resume_skills')

    skill = models.ForeignKey(Skill, null=False, blank=False)

    efficiency_level = models.IntegerField(_('Efficiency Level'), null=False,
                                        blank=False,
                                        validators=[MaxValueValidator(100),
                                                    MinValueValidator(1)])

    def __unicode__(self):
        return "%s (%s)" %(self.resume.user.username, self.skill.name)

    class Meta:
        db_table = 'rm_resume_skill_map'
        verbose_name_plural = 'Resume Skills'
        unique_together = (('resume', 'skill'),)
