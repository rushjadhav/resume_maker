from django import forms
from django.utils.translation import ugettext as _
from django.core.validators import ValidationError

from djangoformsetjs.utils import formset_media_js

from bootstrap3_datepicker.widgets import DatePickerInput
from bootstrap3_datepicker.fields import DatePickerField

class ResumeEducationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.icon_class = 'glyphicon glyphicon-education'
        self.display_name = 'Education'
        self.name = 'education'
        super(ResumeEducationForm, self).__init__(*args, **kwargs)


    institude = forms.CharField(label=_('Institude'), required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Institude', 'class': 'form-control'}))

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

    course_name = forms.CharField(label=_('Course Name'), required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'Course Name', 'class': 'form-control'}))


    def clean(self):
        super(ResumeEducationForm, self).clean()
        from_date = self.cleaned_data.get('from_date')
        to_date = self.cleaned_data.get('to_date')
        if from_date > to_date:
            raise ValidationError('Provided from date must be less than to date.')

    class Media(object):
        js = formset_media_js
