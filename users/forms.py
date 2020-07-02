from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email:")
    reg_no = forms.IntegerField(label="SASTRA Register no:")
    year = forms.IntegerField(label="Year of study")
    dep = forms.CharField(label="Degree & Program")

    class Meta:
        model=User
        fields=['username','email','reg_no','year','dep','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    reg_no = forms.IntegerField(label="SASTRA Register no:")
    year = forms.IntegerField(label="Year of study")
    dep = forms.CharField(label="Degree & Program")
    class Meta:
        model = User
        fields=['username','email','reg_no','year','dep']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
