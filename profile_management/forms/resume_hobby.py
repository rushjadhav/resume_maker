from django import forms
from django.utils.translation import ugettext as _

from djangoformsetjs.utils import formset_media_js

class ResumeHobbyForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.icon_class = 'glyphicon glyphicon-user'
        self.display_name = 'Hobbies'
        self.name = 'hobby'
        super(ResumeHobbyForm, self).__init__(*args, **kwargs)


    hobby = forms.CharField(label=_('Hobby'), required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Hobby', 'class': 'form-control'}))

    efficiency_level = forms.IntegerField(label=_('Efficency Level'), required=True, max_value=100, min_value=1,
                                          widget=forms.TextInput(attrs={'placeholder': 'Efficency Level', 'class': 'form-control'}))

    class Media(object):
        js = formset_media_js
