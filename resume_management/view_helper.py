from django.forms import formset_factory

from profile_management.forms import BasicResumeForm,\
                                     ResumeSkillForm, ResumeLanguageForm,\
                                     ResumeHobbyForm

from education_management.forms import ResumeEducationForm
from experience_management.forms import ResumeExperienceForm

from profile_management.models import Email, PhoneNumber, Address

def get_resume_forms(user, resume):
    forms = []

    basic_data_form = BasicResumeForm(initial=resume.get_basic_details())
    edu_form = ResumeEducationForm()
    experience_form = ResumeExperienceForm()

    SkillFormSet = formset_factory(ResumeSkillForm, extra=0)
    skill_form_set = SkillFormSet(prefix='skills', initial=resume.get_skills_details())

    LanguageFormSet = formset_factory(ResumeLanguageForm, extra=0)
    language_form_set = LanguageFormSet(prefix='languages', initial=resume.get_languages_details())

    HobbyFormSet = formset_factory(ResumeHobbyForm, extra=0)
    hobby_form_set = HobbyFormSet(prefix='hobbies', initial=resume.get_hobbies_details())

    ExperienceFormSet = formset_factory(ResumeExperienceForm, extra=0)
    experience_form_set = ExperienceFormSet(prefix='experiences', initial=resume.get_experience_details())

    EducationFormSet = formset_factory(ResumeEducationForm, extra=0)
    education_form_set = EducationFormSet(prefix='educations', initial=resume.get_education_details())

    forms.append(basic_data_form)
    forms.append(language_form_set)
    forms.append(education_form_set)
    forms.append(experience_form_set)
    forms.append(skill_form_set)
    forms.append(hobby_form_set)

    return forms

def save_basic_details(form, resume):
    objective = form.cleaned_data.get('career_objective')
    email = form.cleaned_data.get('email')
    phone_number = form.cleaned_data.get('phone_number')
    address1 = form.cleaned_data.get('address1')
    address2 = form.cleaned_data.get('address2')
    address3 = form.cleaned_data.get('address3')

    save_objective(resume, objective)
    save_email(resume, email)
    save_phone_number(resume, phone_number)
    save_address(resume, address1, address2, address3)

def save_objective(resume, objective):
    resume.career_objective = objective
    resume.save()

def save_email(resume, email):
    if resume.emails.all():
        obj = resume.emails.all()[0]
        obj.email = email
        obj.save()
    else:
        obj, is_created= Email.objects.get_or_create(email=email)
        resume.emails.add(obj)

def save_phone_number(resume, phone_number):
    if resume.phone_numbers.all():
        obj = resume.phone_numbers.all()[0]
        obj.phone_number = phone_number
        obj.save()
    else:
        obj, is_created = PhoneNumber.objects.get_or_create(phone_number=phone_number)
        resume.phone_numbers.add(obj)

def save_address(resume, address1, address2, address3):
    if resume.addresses.all():
        obj = resume.addresses.all()[0]
        obj.address1 = address1
        obj.address2 = address2
        obj.address3 = address3
        obj.save()
    else:
        obj = Address.objects.create(address1=address1, address2=address2, address3=address3)
        resume.addresses.add(obj)

