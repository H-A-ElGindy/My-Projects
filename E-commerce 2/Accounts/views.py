from django.shortcuts import render,redirect
from .forms import Profile_Form, Register_Form,User_Form,Profile
from.models import Profile,User
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def sign_up(request):
    form=Register_Form(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('accounts:profile')
    else:
        form=Register_Form()
        return render(request,'Accounts/register.html',{'form':form})

def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('accounts:profile')
    else:
        return render(request,'Accounts/login.html')
    return render(request,'Accounts/login.html')

def log_out(request):
    logout(request) 
    return render(request,'Home/Home.html')

def profile(request):
    return render(request,'Accounts/profile.html')

def reset_password(request):
    if request.method=='POST':
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
    return render(request,'Accounts/reset_password.html')

def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform=User_Form(request.POST,request.FILES,instance=request.user)
        profileform=Profile_Form(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('accounts:profile')
    else:
        userform=User_Form(instance=request.user)
        profileform=Profile_Form(instance=profile)
    context={'userform':userform,'profileform':profileform}
    return render(request,'Accounts/edit_profile.html',context)