from django.db import models
from django.utils.translation import ugettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from profile_management.models import Language

class ResumeLanguageMap(models.Model):
    """
    Class representing a mapping between resume and skill.
    """

    resume = models.ForeignKey('Resume', null=False, blank=False,
                               related_name='resume_languages')

    language = models.ForeignKey(Language, null=False, blank=False)

    efficiency_level = models.IntegerField(_('Efficiency Level'), null=False,
                                        blank=False,
                                        validators=[MaxValueValidator(100),
                                                    MinValueValidator(1)])

    def __unicode__(self):
        return "%s (%s)" %(self.resume.user.username, self.language.name)

    class Meta:
        db_table = 'rm_resume_language_map'
        verbose_name_plural = 'Resume Languages'
        unique_together = (('resume', 'language'),)
