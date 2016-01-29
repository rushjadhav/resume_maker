from django import forms
from django.utils.translation import ugettext as _
from django.core.validators import ValidationError

from djangoformsetjs.utils import formset_media_js

from bootstrap3_datepicker.widgets import DatePickerInput
from bootstrap3_datepicker.fields import DatePickerField

class ResumeExperienceForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.icon_class = 'glyphicon glyphicon-user'
        self.display_name = 'Experience'
        self.name = 'experience'
        super(ResumeExperienceForm, self).__init__(*args, **kwargs)


    company = forms.CharField(label=_('Company'), required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control'}))

    from_date = DatePickerField(input_formats=["%d %B %Y"],
                                widget_attrs={"placeholder": "From Date",
                                              "class": "form-control"},
                                widget_options={"minViewMode": "dates",
                                                "autoclose": True})


    to_date = DatePickerField(input_formats=["%d %B %Y"],
                              widget_attrs={"placeholder": "To Date",
                                            "class": "form-control"},
                              widget_options={"minViewMode": "dates",
                                              "autoclose": True})

    designation = forms.CharField(label=_('Designation'), required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'Designation', 'class': 'form-control'}))


    def clean(self):
        super(ResumeExperienceForm, self).clean()
        from_date = self.cleaned_data.get('from_date')
        to_date = self.cleaned_data.get('to_date')
        if from_date > to_date:
            raise ValidationError('Provided from date must be less than to date.')

    class Media(object):
        js = formset_media_js
