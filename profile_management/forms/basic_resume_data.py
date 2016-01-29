from django import forms
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

class BasicResumeForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.icon_class = 'glyphicon glyphicon-user'
        self.display_name = 'Personal Details'
        self.name = 'basic_details'

        super(BasicResumeForm, self).__init__(*args, **kwargs)


    career_objective = forms.CharField(label=_('Career Objective'),
                                       required=True,
                                       widget=forms.TextInput(attrs={'placeholder': 'Career Objective',
                                                                      'class':'form-control'}))

    email = forms.EmailField(label=_('Email'),
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                          'class':'form-control'}))
    phone_number = forms.CharField(label=_('Phone Number'),
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'Phone Number',
                                                                  'class':'form-control'}))
    address1 = forms.CharField(label=_('Address1'),
                                      required=False,
                                      widget=forms.TextInput(attrs={'placeholder': 'Address1',
                                                                  'class':'form-control'}))
    address2 = forms.CharField(label=_('Address2'),
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'Address2',
                                                                  'class':'form-control'}))
    address3 = forms.CharField(label=_('Address3'),
                                required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Address3',
                                                              'class':'form-control'}))
