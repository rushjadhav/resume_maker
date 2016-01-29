from django import forms
from django.utils.translation import ugettext as _

from djangoformsetjs.utils import formset_media_js

class ResumeSkillForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.icon_class = 'glyphicon glyphicon-user'
        self.display_name = 'Skills'
        self.name = 'skill'
        super(ResumeSkillForm, self).__init__(*args, **kwargs)


    skill = forms.CharField(label=_('Skill'), required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Skill', 'class': 'form-control'}))

    efficiency_level = forms.IntegerField(label=_('Efficency Level'), required=True, max_value=100, min_value=1,
                                          widget=forms.TextInput(attrs={'placeholder': 'Efficency Level', 'class': 'form-control'}))

    class Media(object):
        js = formset_media_js
