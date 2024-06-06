from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Profile,User,Application
from .forms import Register_Form,User_Form,Profile_Form,Application_Form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    form=Register_Form(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            return render (request,'Accounts/profile.html')
    form=Register_Form()
    return render(request,'Accounts/register.html',{'form':form})       

def Login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return render(request,'Accounts/profile.html')
        return render(request,'Accounts/login.html')    
    return render(request,'Accounts/login.html')

def Logout(request):
    logout(request)
    return redirect('Home:home') 

def reset_password(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password1']
        password2=request.POST['password2']
        if password==password2:
            user_exist=User.objects.filter(email=email).exists()
            if user_exist==True:
                user=User.objects.get(email=email)
                user.set_password(password)
                user.save()
                return redirect('accounts:login')
    return render(request,'accounts/reset_password.html')
    
def profile(request):
    return render (request,'Accounts/profile.html')

def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=="POST":
        user_form=User_Form(request.POST,request.FILES,instance=request.user)
        profile_form=Profile_Form(request.POST,request.FILES,instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request,'Accounts/profile.html')
    user_form=User_Form(instance=request.user) 
    profile_form=Profile_Form(instance=profile)
    context={'userform':user_form,'profileform':profile_form}
    return render(request,'Accounts/edit_profile.html',context)

@login_required(login_url='accounts:login')
def application(request):
    application=Application()
    application.user=request.user
    if request.method=="POST":
        course=request.POST['course']
        form=Application_Form(request.POST,request.FILES,instance=application)
        if form.is_valid():
            application_exist=Application.objects.filter(user=request.user,course=course).exists()
            if application_exist==True:
                return HttpResponse('Application Submitted Before') 
            form.save()
            return HttpResponse('Application Submitted')
        
    form=Application_Form(instance=application)
    return render(request,'Application/application.html',{'form':form})
   
