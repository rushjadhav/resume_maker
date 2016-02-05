from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import formset_factory
from django.db import IntegrityError

from resume_management.models import ResumeTemplate, Resume, ResumeSkillMap,\
                                     ResumeLanguageMap, ResumeHobbyMap
from resume_management.forms import CreateResumeForm, PublishResumeForm
from resume_management.view_helper import get_resume_forms, save_basic_details

from profile_management.forms import BasicResumeForm, ResumeSkillForm,\
                                     ResumeLanguageForm, ResumeHobbyForm

from profile_management.models import Skill, Language, Hobby
from experience_management.forms import ResumeExperienceForm
from experience_management.models import Company, Experience

from education_management.forms import ResumeEducationForm
from education_management.models import Institude, Education

from utils import get_random_string, is_form_set, render_to_pdf

class ListTemplatesView(View):

    def get(self, request):
        """
        """

        templates = ResumeTemplate.objects.filter(status='A')
        return render(request, 'rm_templates.html', {'templates': templates})

class CreateResumeView(View):

    def get(self, request):
        form = CreateResumeForm()
        return render(request, 'create_resume.html', {'form': form})

    def post(self, request):
        form = CreateResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.access_url = get_random_string(16)
            resume.save()
            return HttpResponseRedirect(reverse('resume:update_resume',
                                                args=(resume.name,)))
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'create_resume.html', {'form': form})

class PublishResumeView(View):

    def get(self, request, id):
        try:
            resume = Resume.objects.get(pk=id)
            form = PublishResumeForm(initial={'access_url': resume.access_url,
                                              'resume_template': resume.resume_template})
            return render(request, "publish_resume.html", {'form': form,
                                                           'resume': resume})
        except Resume.DoesNotExist:
            raise Http404

    def post(self, request, id):

        try:
            resume = Resume.objects.get(pk=id)
            form = PublishResumeForm(request.POST)
            if form.is_valid():
                try:
                    resume.is_published = True
                    resume.resume_template = form.cleaned_data['resume_template']
                    resume.access_url = form.cleaned_data['access_url']
                    resume.save()
                    messages.success(request, 'Your resume published successfully.')
                    messages.success(request, 'Share this url with any body "%s"' %(resume.access_url))
                    return HttpResponseRedirect(reverse("dashboard:index"))
                except IntegrityError as inst:
                    messages.error(request, inst.message)
            return render(request, "publish_resume.html", {'form': form,
                                                           'resume': resume})
        except Resume.DoesNotExist:
            raise Http404

class PreviewTemplateView(View):

    def get(self, request, id):
        try:
            template = ResumeTemplate.objects.get(pk=id)
            return render(request, "resume_templates/demo/%s.html" %(template.code))
        except ResumeTemplate.DoesNotExist:
            raise Http404

class LivePreviewView(View):

    def get(self, request, template_id, resume_id):
        try:
            template = ResumeTemplate.objects.get(pk=template_id)
            resume = Resume.objects.get(pk=resume_id)
            return render(request,
                          "resume_templates/%s.html" %(template.name),
                          {'resume': resume, 'show_back': True})

        except ResumeTemplate.DoesNotExist, Resume.DoesNotExist:
            raise Http404

class DisplayResume(View):

    def get(self, request, access_url):

        try:
            resume = Resume.objects.get(access_url=access_url)
            resume.update_number_of_views(request.user)
            return render(request,
                          "resume_templates/%s.html" %(resume.resume_template.code),
                          {'resume': resume})
        except Resume.DoesNotExist:
            raise Http404

class UpdateResumeView(View):

    def get_resume(self, request, name):
        return Resume.objects.get(user=request.user, name=name)

    def get(self, request, name):
        try:
            resume = self.get_resume(request, name)
            forms = get_resume_forms(request.user, resume)
            return render(request, 'update_resume.html', {'resume': resume,
                                                          'forms': forms,
                                                          'form_name': forms[0].name})
        except Resume.DoesNotExist:
            raise Http404

    def post(self, request, name):

        form_name = request.POST.get('form_name')
        resume = self.get_resume(request, name)
        has_errors = False

        if form_name == 'basic_details':
            current_form = BasicResumeForm(request.POST)
            if current_form.is_valid():
                save_basic_details(current_form, resume)
                messages.success(request, 'Personal Details saved successfully.')
            else:
               has_errors = True
               messages.error(request, 'Please correct the errors below.')

        elif form_name == 'skill':
           ResumeSkillFormSet = formset_factory(ResumeSkillForm)
           current_form = ResumeSkillFormSet(request.POST, request.FILES, prefix='skills')
           if current_form.is_valid():
               resume.resume_skills.all().delete()
               for form in current_form:
                   if (form in current_form.extra_forms and form.has_changed()) or form in current_form.initial_forms :
                       skill = form.cleaned_data['skill']
                       efficiency_level = form.cleaned_data['efficiency_level']
                       obj, is_created = Skill.objects.get_or_create(name=skill)
                       try:
                           ResumeSkillMap.objects.create(skill=obj, resume=resume,
                                                         efficiency_level=efficiency_level)
                       except IntegrityError as inst:
                           has_errors = True
                           messages.error(request, 'Skill %s is already present' %(skill))

               messages.success(request, 'Skills saved successfully.')
           else:
               has_errors = True
               messages.error(request, 'Please correct the errors below.')

        elif form_name == 'language':
           ResumeLanguageFormSet = formset_factory(ResumeLanguageForm)
           current_form = ResumeLanguageFormSet(request.POST, request.FILES, prefix='languages')
           if current_form.is_valid():
               resume.resume_languages.all().delete()
               for form in current_form:
                   if (form in current_form.extra_forms and form.has_changed()) or form in current_form.initial_forms :
                       language = form.cleaned_data['language']
                       efficiency_level = form.cleaned_data['efficiency_level']
                       obj, is_created = Language.objects.get_or_create(name=language)
                       try:
                           ResumeLanguageMap.objects.create(language=obj, resume=resume,
                                                            efficiency_level=efficiency_level)
                       except IntegrityError as inst:
                           has_errors = True
                           messages.error(request, 'Language %s is already present' %(language))
               messages.success(request, 'Languages saved successfully.')
           else:
               has_errors = True
               messages.error(request, 'Please correct the errors below.')


        elif form_name == 'hobby':
           ResumeHobbyFormSet = formset_factory(ResumeHobbyForm)
           current_form = ResumeHobbyFormSet(request.POST, request.FILES, prefix='hobbies')
           if current_form.is_valid():
               resume.resume_hobbies.all().delete()
               for form in current_form:
                   if (form in current_form.extra_forms and form.has_changed()) or form in current_form.initial_forms :
                       hobby = form.cleaned_data['hobby']
                       efficiency_level = form.cleaned_data['efficiency_level']
                       obj, is_created = Hobby.objects.get_or_create(name=hobby)
                       try:
                           ResumeHobbyMap.objects.create(hobby=obj, resume=resume,
                                                         efficiency_level=efficiency_level)
                       except IntegrityError as inst:
                           has_errors = True
                           messages.error(request, 'Hobby %s is already present' %(hobby))

               messages.success(request, 'Hobbies saved successfully.')
           else:
               has_errors = True
               messages.error(request, 'Please correct the errors below.')

        elif form_name == 'experience':
           ResumeExperienceFormSet = formset_factory(ResumeExperienceForm)
           current_form = ResumeExperienceFormSet(request.POST, request.FILES, prefix='experiences')
           if current_form.is_valid():
               resume.resume_experiences.all().delete()
               for form in current_form:
                   if (form in current_form.extra_forms and form.has_changed()) or form in current_form.initial_forms :
                       company = form.cleaned_data['company']
                       designation = form.cleaned_data['designation']
                       from_date = form.cleaned_data['from_date']
                       to_date = form.cleaned_data['to_date']
                       obj, is_created = Company.objects.get_or_create(name=company)
                       try:
                           Experience.objects.create(company=obj, resume=resume,
                                                     from_date=from_date, to_date=to_date,
                                                     designation=designation)
                       except IntegrityError as inst:
                           has_errors = True
                           messages.error(request, 'Company %s is already present' %(compnay))
               messages.success(request, 'Experiences saved successfully.')
           else:
               has_errors = True
               messages.error(request, 'Please correct the errors below.')

        elif form_name == 'education':
           ResumeEducationFormSet = formset_factory(ResumeEducationForm)
           current_form = ResumeEducationFormSet(request.POST, request.FILES, prefix='educations')
           if current_form.is_valid():
               resume.resume_educations.all().delete()
               for form in current_form:
                   if (form in current_form.extra_forms and form.has_changed()) or form in current_form.initial_forms :
                       institude = form.cleaned_data['institude']
                       course_name = form.cleaned_data['course_name']
                       from_date = form.cleaned_data['from_date']
                       to_date = form.cleaned_data['to_date']
                       obj, is_created = Institude.objects.get_or_create(name=institude)
                       try:
                           Education.objects.create(institude=obj, resume=resume,
                                                    from_date=from_date, to_date=to_date,
                                                    course_name=course_name)
                       except IntegrityError as inst:
                           has_errors = True
                           messages.error(request, 'Institude %s is already present' %(institude))
               messages.success(request, 'Educations saved successfully.')
           else:
               has_errors = True
               messages.error(request, 'Please correct the errors below.')

        forms = get_resume_forms(request.user, resume)
        if has_errors:
            new_forms = []
            for form in forms:
                if is_form_set(form) and form[0].name == form_name:
                    new_forms.append(current_form)
                elif not is_form_set(form) and form.name == form_name:
                    new_forms.append(current_form)
                else:
                    new_forms.append(form)
        else:
            new_forms = forms
            try:
                form_name = get_next_form(new_forms, form_name)
            except IndexError:
                return HttpResponseRedirect(reverse('resume:publish_resume', args=[resume.id]))
        return render(request, 'update_resume.html',
                      {'resume': resume, 'forms': new_forms,
                       'form_name': form_name})

def get_next_form(new_forms, form_name):

    for index, form in enumerate(new_forms):
        if is_form_set(form):
            if form[0].name == form_name:
                next_form = new_forms[index+1]
                if is_form_set(next_form):
                    return next_form[0].name
                else:
                    return next_form.name
        else:
            if form.name == form_name:
                next_form = new_forms[index+1]
                if is_form_set(next_form):
                    return next_form[0].name
                else:
                    return next_form.name

class ResumePDFView(View):

    def get(self, request, id):
        try:
            resume = Resume.objects.get(pk=id)
            resume_template_path = "resume_templates/pdf/%s.html" %(resume.resume_template.name)
            return render_to_pdf(resume_template_path,{'resume': resume,})
        except Resume.DoesNotExist:
            raise Http404
