from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import RegisterUser,userQuestion

GENDER_CHOICES = (
   ('Male','Male'),
   ('Female','Female'),
   ('Other','Other')  
)

class RegisterUserForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=GENDER_CHOICES)
    class Meta:
        model = RegisterUser
        fields = '__all__'


class userQuestionForm(forms.ModelForm):
    class Meta:
        model = userQuestion
        fields = '__all__'

    