from django.forms import ModelForm
from django import forms
from .models import Student


class StudentForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField()

    class Meta:
        model = Student
        fields = [
            'username',
            'password',
            'firstname',
            'lastname',
            'course',
            'department'
        ]