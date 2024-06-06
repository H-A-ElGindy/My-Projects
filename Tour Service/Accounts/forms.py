from django import forms
from .models import Profile,User
from django.contrib.auth.forms import UserCreationForm

class Register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class User_form(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']

class Profile_form(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = "__all__"
        exclude= 'user',

