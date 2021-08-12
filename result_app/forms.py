from django import forms
from secondary.models import Student


class ResultForm(forms.ModelForm):
    term = forms.CharField(widget=forms.TextInput(),required=True, max_length=100)
    studentname = forms.CharField(widget=forms.TextInput(),required=True, max_length=100)
    Class = forms.CharField(widget=forms.TextInput(),required=True, max_length=100)
    subject = forms.CharField(widget=forms.TextInput(),required=False, max_length=100)
    firstCA = forms.IntegerField(widget=forms.TextInput(),required=False)
    secondCA = forms.IntegerField(widget=forms.TextInput(),required=False)
    thirdCA = forms.IntegerField(widget=forms.TextInput(),required=False)
    exams = forms.IntegerField(widget=forms.TextInput(),required=False)
    total = forms.IntegerField(widget=forms.TextInput(), required=False)

    class Meta:
        model = Student
        fields = ['studentname', 'term', 'Class', 'firstCA', 'secondCA', 'thirdCA', 'exams', 'total']