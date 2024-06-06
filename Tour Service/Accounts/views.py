from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import User,Profile
from . forms import Register_form,User_form,Profile_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    form=Register_form(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            return redirect("Accounts:profile")       
    form=Register_form()
    return render(request,'Accounts/register.html',{'form':form})      

def Login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("Accounts:profile")
        return render(request,'Accounts/login.html')
    return render(request,'Accounts/login.html')

def log_out(request):
    logout(request)
    return render(request,'Home/Home.html')

def reset_password(request):
    if request.method=="POST":
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            email_exists=User.objects.filter(email=email).exists()
            if email_exists==True:
                user=User.objects.get(email=email)
                user.set_password(password1)
                user.save()
                return redirect('Accounts:login')
            else:
                return HttpResponse('Email Does not exist')
        else:
            return HttpResponse('Passwords do not match')     
    return render (request,'Accounts/reset_password.html')

@login_required(login_url="Accounts:login")
def profile(request):
    return render(request,'Accounts/profile.html')

def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=="POST":
        user_form=User_form(request.POST,request.FILES,instance=request.user)
        profile_form=Profile_form(request.POST,request.FILES,instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request,'Accounts/profile.html')
    user_form=User_form(instance=request.user)
    profile_form=Profile_form(instance=profile)
    return render(request,'Accounts/edit_profile.html',{'userform':user_form,'profileform':profile_form})