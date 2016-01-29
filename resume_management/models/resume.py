from django.db import models
from django.utils.translation import ugettext as _

from utils.choices import STATUS_CHOICES

from profile_management.models import UserProfile, Address, Email, PhoneNumber

class Resume(models.Model):
    """
    Class representing a Resume.
    """

    name = models.CharField(_('Name'), max_length=60, null=False, blank=False,
                            unique=True)

    user = models.ForeignKey(UserProfile, related_name='resumes', null=False,
                             blank=False)

    resume_template = models.ForeignKey('ResumeTemplate',
                                        related_name='template_resumes',
                                        null=True, blank=True)

    is_published = models.BooleanField(_('Share'), default=False, null=False,
                                       blank=False)

    access_url = models.CharField(_('Access Url'), max_length=120,
                                 null=False, blank=False, unique=True)

    number_of_views = models.IntegerField(_('Number Of Views'), null=False,
                                    blank=False, default=0)

    career_objective = models.TextField(_('Career objective'), null=True,
                                       blank=True)

    emails = models.ManyToManyField(Email)

    addresses = models.ManyToManyField(Address)

    phone_numbers = models.ManyToManyField(PhoneNumber)

    status = models.CharField(_('Status'), max_length=1, null=False,default='A',
                              blank=False, choices= STATUS_CHOICES)

    def get_completed_percentage(self):
        total_forms = 6.0
        completed_forms = 0.0

        if self.get_education_details():
            completed_forms+=1.0
        if self.get_experience_details():
            completed_forms+=1.0
        if self.get_hobbies_details():
            completed_forms+=1.0
        if self.get_skills_details():
            completed_forms+=1.0
        if self.get_languages_details():
            completed_forms+=1.0
        if self.get_basic_details():
            completed_forms+=1.0

        return int(completed_forms / total_forms * 100)

    def get_education_details(self):
        details = []
        for resume_education in self.resume_educations.all():
            resume_education_detail = {}
            resume_education_detail['institude'] = resume_education.institude.name
            resume_education_detail['from_date'] = resume_education.from_date
            resume_education_detail['to_date'] = resume_education.to_date
            resume_education_detail['course_name'] = resume_education.course_name
            details.append(resume_education_detail)
        return details

    def get_experience_details(self):
        details = []
        for resume_experience in self.resume_experiences.all():
            resume_experience_detail = {}
            resume_experience_detail['company'] = resume_experience.company.name
            resume_experience_detail['from_date'] = resume_experience.from_date
            resume_experience_detail['to_date'] = resume_experience.to_date
            resume_experience_detail['designation'] = resume_experience.designation
            details.append(resume_experience_detail)
        return details

    def get_hobbies_details(self):
        details = []
        for resume_hobby in self.resume_hobbies.all():
            resume_hobby_detail = {}
            resume_hobby_detail['hobby'] = resume_hobby.hobby.name
            resume_hobby_detail['efficiency_level'] = resume_hobby.efficiency_level
            details.append(resume_hobby_detail)
        return details

    def get_skills_details(self):
        details = []
        for resume_skill in self.resume_skills.all():
            resume_skill_detail = {}
            resume_skill_detail['skill'] = resume_skill.skill.name
            resume_skill_detail['efficiency_level'] = resume_skill.efficiency_level
            details.append(resume_skill_detail)
        return details

    def get_languages_details(self):
        details = []
        for resume_language in self.resume_languages.all():
            resume_language_detail = {}
            resume_language_detail['language'] = resume_language.language.name
            resume_language_detail['efficiency_level'] = resume_language.efficiency_level
            details.append(resume_language_detail)
        return details

    def get_basic_details(self):

        details = {}
        if self.career_objective:
            details['career_objective'] = self.career_objective

        if self.emails.all():
            details['email'] = self.emails.all()[0].email
        if self.phone_numbers.all():
            details['phone_number'] = self.phone_numbers.all()[0].phone_number

        if self.addresses.all():
            details['address1'] = self.addresses.all()[0].address1
            details['address2'] = self.addresses.all()[0].address2
            details['address3'] = self.addresses.all()[0].address3

        return details


    def update_number_of_views(self, user):
        if not user == self.user:
            self.number_of_views +=1
            self.save()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'rm_resume'
        verbose_name_plural = 'Resumes'
        unique_together = (('user', 'name'),)
