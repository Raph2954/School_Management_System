from django.contrib.auth.models import User
from django import forms
from secondary.models import Teacher


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

#user registration
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('passwords don\'t match, try again.')
        return cd['password2']


