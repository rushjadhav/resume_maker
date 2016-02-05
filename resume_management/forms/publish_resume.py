from django import forms
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from resume_management.models import ResumeTemplate

class PublishResumeForm(forms.Form):

    access_url = forms.CharField(label=_('Sub url'),
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Sub Url',
                                                               'class':'form-control'}))

    resume_template = forms.ModelChoiceField(queryset=ResumeTemplate.objects.all(),
                                             label=_('Select Template'), required=True)
