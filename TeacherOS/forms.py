from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import *


class User_form(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))
    is_superuser = forms.BooleanField(required = False, widget=forms.widgets.CheckboxInput())

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1','password2', 'is_superuser']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class HWForm(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = '__all__'

class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class ReportForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = '__all__'
