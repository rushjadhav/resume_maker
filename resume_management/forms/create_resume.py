from django import forms

from resume_management.models import Resume

class CreateResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('name',)
        widgets={
            "name": forms.TextInput(attrs={'placeholder':'Name',
                                                 'class': 'form-control'})
        }
