
from django.shortcuts import redirect, render
from .forms import RegisterForm,UserForm,ProfileForm
from .models import Profile,User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register (request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request, username=username,password=password)
            login(request,user)
            return redirect('accounts:profile')
    else:
        form=RegisterForm()   
    
    return render(request,'accounts/register.html',{'form':form})
  

def log_in(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('accounts:profile')
    else:
        return render(request,'accounts/login.html')
    return render(request,'accounts/login.html')
            
    
def profile(request):
    return render(request,'accounts/profile.html')

def log_out(request):
    logout(request)
    return render(request,'home/home.html')

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
 
def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=="POST":
        u=UserForm(request.POST,request.FILES,instance=request.user)
        p=ProfileForm(request.POST,request.FILES,instance=profile)
        if u.is_valid() and p.is_valid():
            u.save()
            p.save()
            return redirect('accounts:profile')    
    else:
       u=UserForm(instance=request.user)
       p=ProfileForm(instance=profile)
    context={'userform':u,'profileform':p}
    return render(request,'accounts/edit_profile.html',context)