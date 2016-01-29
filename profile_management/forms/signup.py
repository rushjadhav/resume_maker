import datetime

from django import forms
from django.core.validators import ValidationError

from bootstrap3_datepicker.fields import DatePickerField

class SignUpForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs= {'placeholder': 'User Name',
                                                              'class': 'form-control',
                                                              'autofocus': 'true'}))

    first_name = forms.CharField(widget=forms.TextInput(attrs= {'placeholder': 'First Name',
                                                              'class': 'form-control'}))

    middle_name = forms.CharField(required=False,
                                  widget=forms.TextInput(attrs={'placeholder': 'Middle Name',
                                                                'class': 'form-control'}))

    last_name = forms.CharField(required=False,
                                widget=forms.TextInput(attrs= {'placeholder': 'Last Name',
                                                               'class': 'form-control'}))

    email = forms.EmailField(widget=forms.TextInput(attrs= {'placeholder': 'Email',
                                                           'class': 'form-control'}))

    date_of_birth = DatePickerField(input_formats=["%d %B %Y"],
                                    widget_attrs={"placeholder": "Date of Birth",
                                                  "class": "form-control"},
                                    widget_options={"minViewMode": "dates",
                                                    "autoclose": True})

    password = forms.CharField(widget=forms.PasswordInput(attrs= {'placeholder': 'Password',
                                                              'class': 'form-control'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs= {'placeholder': 'Confirm Password',
                                                                          'class': 'form-control'}))


    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Password and confirm password doesn\'t match.')

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        now = datetime.datetime.now().date()
        if now < dob:
            raise ValidationError("Provided date of birth is not valid.")
        return dob
