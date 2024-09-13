from re import L
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from . models import*
from django.contrib import messages
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.decorators import login_required
#user activation imports
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator,PasswordResetTokenGenerator 


def signup(request):
    if request.method=="POST":
        first_name=request.POST['f_name']
        last_name=request.POST['l_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        role=request.POST['role']
        if password1==password2:
            if role=='user' or role=='coach':
                user_exists=User.objects.filter(email=email).first()
                if user_exists:
                    messages.warning(request,'User already registered')
                    return HttpResponseRedirect('/accounts/signup/')
                else:
                    username=email.split('@')[0]
                    user=User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
                    user.set_password(password1) # to hash the password
                    user.is_active=False
                    user.save()
                    profile=Profile.objects.get(user=user)
                    profile.first_name=user.first_name
                    profile.last_name=user.last_name
                    profile.email=user.email
                    profile.role=role
                    profile.save()
                    if user.is_active==False:
                        uidb64=urlsafe_base64_encode(force_bytes(user.pk))
                        current_site=get_current_site(request)
                        token=default_token_generator.make_token(user)
                        send_mail(
                            'Verify email to activate account',
                            f'Hello {user.username} you are receiving this email because you requested to activate your account\nClick the link below to activate your account\n{current_site}/accounts/activate/{uidb64}/{token}',
                            settings.EMAIL_HOST_USER,
                            [user.email],
                            fail_silently=False,)
                        return render(request,'accounts/activate.html')
                    messages.warning(request,'User already activated')
                    return HttpResponseRedirect('/accounts/signup/')
        messages.warning(request,'Passwords do not match')
        return HttpResponseRedirect('/accounts/signup/')       
    return render(request,'accounts/signup.html')


def Activate_account(request,uidb64,token):
    user_id=urlsafe_base64_decode(uidb64).decode()
    try:
        user=User.objects.get(id=int(user_id))
        profile=Profile.objects.get(user=user)
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            login(request,user)
            return render(request,'accounts/profile.html',{'profile':profile})
        else:
            profile=Profile.objects.get(user=user)
            profile.delete()
            user.delete()
            messages.warning(request,'account is not activated')
            return HttpResponseRedirect('/accounts/signup/')   
    except:
        messages.warning(request,'user is not found')
        return HttpResponseRedirect('/accounts/signup/')   


def login_view(request):
    if request.method=="POST":
        email=request.POST['email']
        user_password=request.POST['password']
        user_email = User.objects.filter(email=email).first()
        if not user_email:
            messages.warning(request,'User Does not exist')
            return HttpResponseRedirect('/accounts/login-view/') 
        user=authenticate(request,username=user_email.username,password=user_password)# because password is hashed we need to use authenticate 
        login(request,user) # to save login state and get request.user after login
        if user:
            profile=Profile.objects.filter(user=user).first()
            if profile:
                return render(request,'accounts/profile.html',{'profile':profile})
            else:
                messages.success(request,'User logged in')
                return redirect('accounts:home')
        messages.warning(request,'Wrong Email or password')
        return HttpResponseRedirect('/accounts/login-view/')                                                
    return render(request,'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login_view')


def Reset_Email(request):
    if request.method=="POST":
        user_request=request.user
        email=request.POST['email']
        user=User.objects.get(username=user_request,email=email)
        if user:
            uidb64=urlsafe_base64_encode(force_bytes(user.pk))
            current_site=get_current_site(request)
            token=default_token_generator.make_token(user)
            send_mail(
            'Reset Password Email',
            f'Hello {user.username} you are receiving this email because you requested to reset your password\nClick the link below to reset your password\n{current_site}/accounts/reset_password/{uidb64}/{token}',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,)
            return render(request,'accounts/instructions.html')
        messages.warning(request,'Wrong Email')
        return HttpResponseRedirect('/accounts/reset-email/')            
    return render(request,'accounts/email_verify.html')


def Reset_password(request,uidb64,token):
    user_id=urlsafe_base64_decode(uidb64).decode()
    try:
        user=User.objects.get(id=int(user_id))
        if default_token_generator.check_token(user,token):
            if request.method=='POST':
                password1=request.POST['password1']
                password2=request.POST['password2']
                if password1==password2:
                    user.set_password(password1)
                    user.save()
                    return redirect('accounts:login_view')
            return render(request,'accounts/reset_password.html')
        messages.warning(request,'Invalid Token')
        return HttpResponseRedirect('/accounts/reset-email/') 
    except:
        messages.warning(request,'User not found')
        return HttpResponseRedirect('/accounts/reset-email/') 


@login_required(login_url='accounts:login_view')
def profile(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if profile:
        return render (request,'accounts/profile.html',{'profile':profile})
    return redirect('accounts:home')


def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=="POST":
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        email=request.POST['email']
        email_exists=User.objects.filter(email=email).exclude(username=request.user)
        if email_exists:
            messages.warning(request,'Email exists for another user')
            return HttpResponseRedirect('/accounts/edit-profile/')  
        phone=request.POST['phone']
        designation=request.POST['title']
        biography=request.POST['biography']
        facebook=request.POST['facebook']
        linkedin=request.POST['linkedin']
        # to solve edit profile image
        if 'image' in request.FILES:
            profile.image = request.FILES['image']
            profile.save()
        profile.first_name=f_name
        profile.last_name=l_name
        profile.email=email
        profile.phone=phone
        profile.designation=designation
        profile.facebook=facebook
        profile.linkedin=linkedin
        profile.biography=biography
        profile.save()
        return render(request,'accounts/profile.html',{'profile':profile})
    return render(request,'accounts/edit_profile.html',{'profile':profile})
    

def upload_post(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method=="POST":
        title=request.POST['title']
        description=request.POST['description']
        post=Post.objects.create(profile=profile,title=title,description=description)
        if 'file' in request.FILES:
            post.file = request.FILES['file']
            post.save()
        return redirect('accounts:profile')
    return render(request,'accounts/upload_post.html',{'profile':profile})   


