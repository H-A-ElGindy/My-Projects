from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,User,Application

class Register_Form(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class User_Form(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email')

class Profile_Form(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude= 'user',

class Application_Form(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        exclude= 'user',