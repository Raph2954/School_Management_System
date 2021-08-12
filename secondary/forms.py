from django import forms
#from .models import Result1, Result2, Result3
from django.contrib.auth.models import User
from secondary.models import Student, Teacher


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('Photo', 'Sex', 'Address', 'Qualification', 'Subjects_Handling', 'Admin_Role','State_of_origin',)









