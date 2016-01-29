from django import forms

class SignInForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs= {'placeholder': 'username',
                                                              'class': 'form-control',
                                                              'autofocus': 'true'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs= {'placeholder': 'password',
                                                                  'class': 'form-control'}))


