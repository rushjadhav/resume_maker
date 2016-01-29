from django import forms
from django.core.validators import ValidationError

from bootstrap3_datepicker.widgets import DatePickerInput
from bootstrap3_datepicker.fields import DatePickerField

from profile_management.models import UserProfile

class ProfileForm(forms.ModelForm):

    date_of_birth = DatePickerField(input_formats=["%d %B %Y"],
                                    widget_attrs={"placeholder": "Date of Birth",
                                                  "class": "form-control"},
                                    widget_options={"minViewMode": "dates",
                                                    "autoclose": True})

    class Meta:
        model = UserProfile
        fields = ('first_name', 'middle_name', 'last_name', 'email',
                  'date_of_birth', 'profile_pic', 'nationality',)
        widgets={
            "first_name": forms.TextInput(attrs={'placeholder':'First Name',
                                                 'class':'form-control'}),

            "middle_name": forms.TextInput(attrs={'placeholder':'Middle Name',
                                                  'class':'form-control'}),

            "last_name": forms.TextInput(attrs={'placeholder':'Last Name',
                                                'class':'form-control'}),

            "email": forms.TextInput(attrs={'placeholder':'Email',
                                            'class':'form-control'}),

            "nationality": forms.TextInput(attrs={'placeholder':'Nationality',
                                            'class':'form-control'}),

        }

