# django imports
import re
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
# user activation 
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator,PasswordResetTokenGenerator 
# rest framework imports
from rest_framework.authtoken.models import Token
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
# serializer imports
from . serializers import *
# models import
from accounts.models import *


class Signup(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            password1=request.data['password']
            first_name=self.request.data['first_name']
            last_name=self.request.data['last_name']
            email=self.request.data['email']
            role=self.request.data['role']
            if role=='user' or role=='coach':
                user_exists=User.objects.filter(email=email).first()
                if user_exists:
                    return Response({'message':'user exists','serializer':serializer.data},status=status.HTTP_226_IM_USED)
                username=email.split('@')[0]
                user=User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
                user.set_password(password1) # hash password
                user.is_active=False
                user.save()
                profile=Profile.objects.get(user=user)
                profile.first_name=user.first_name
                profile.last_name=user.last_name
                profile.email=user.email
                profile.role=role
                profile.save()
                # Activate account email
                if user.is_active==False:
                    current_site=get_current_site(request)
                    uidb64=urlsafe_base64_encode(force_bytes(user.pk))
                    token=default_token_generator.make_token(user)
                    send_mail(
                    'Verify Email to Activate Account',
                    f'Hello {user.username} you are receiving this email because you requested to activate your account\nClick the link below to activate your account \n{current_site}/accounts/api-activate/{uidb64}/{token}',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                    )
                    return Response({'message':'Check your email for instructions'},status=status.HTTP_202_ACCEPTED)  
                else:
                    return Response({'message':'user is already activated'},status=status.HTTP_403_FORBIDDEN)                   
        return Response(serializer.errors)


class ActivateAccount(APIView):
    def post(self,request,uidb64,token):
        user_id=urlsafe_base64_decode(uidb64).decode()
        try:
            user=User.objects.get(id=int(user_id)) # must always change to int
            if default_token_generator.check_token(user,token):
                user.is_active=True
                user.save()
                token= token, created = Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'message':'Account activated','token':token.key},status=status.HTTP_201_CREATED)      
            profile=Profile.objects.get(user=user)
            profile.delete()
            user.delete()
            return Response({'message':'Invalid user or Token'},status=status.HTTP_404_NOT_FOUND) 
        except:
            return Response({'message':'User does not exist'},status=status.HTTP_404_NOT_FOUND)

   
class Login(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            try:
                user_email=User.objects.get(email=email) # to be able to use username
                user=authenticate(request,username=user_email.username,password=password) # to use username and password is hashed
                token, created = Token.objects.get_or_create(user=user)
                json={'message':'login success','token':token.key}
                return Response(json,status=status.HTTP_200_OK)
            except:
                return Response({'message':'user does not exist'},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors)


class Logout(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response({'message':'user logged out'},status=status.HTTP_200_OK)


class ChangeUserPassword(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request,profile_slug):
        serializer=ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_pass=serializer.validated_data['old_password']
            new_password=serializer.validated_data['new_password']
            confirm_password=serializer.validated_data['confirm_password']
            user=self.request.user
            try:
                profile=Profile.objects.get(user=user,profile_slug=profile_slug)
                check_user=authenticate(request,username=profile.user,password=old_pass)
                if not check_user:
                    return Response({'message':'old password is wrong'},status=status.HTTP_406_NOT_ACCEPTABLE)
                if new_password==confirm_password:
                    check_user.set_password(new_password)
                    check_user.save()
                    return Response({'message':'Password change success'},status=status.HTTP_200_OK)
                return Response({'message':'Password do not match'},status=status.HTTP_406_NOT_ACCEPTABLE)
            except:
                return Response({'message':'Invalid User'},status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors)


class RequestPasswordResetEmail(generics.GenericAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=RequestPasswordResetEmailSerializer
    def post(self, request,profile_slug):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_email=request.data['email']
            user=self.request.user
            try:
                user_request=User.objects.get(username=user,email=user_email)
                profile=Profile.objects.get(user=user_request,profile_slug=profile_slug)
                if profile:
                    uidb64=urlsafe_base64_encode(force_bytes(user.id)) # secure user id 
                    token=PasswordResetTokenGenerator().make_token(user) # generate token for user
                    #verify email using our site domain
                    current_site=get_current_site(request)
                    #send mail in this section
                    send_mail(
                    'Verify Email to Reset Password',
                    f'Hello {user.username} you are receiving this email because you requested to reset your password\nClick the link below to reset your password \n{current_site}/accounts/{profile_slug}/request_password/{uidb64}/{token}',
                    settings.EMAIL_HOST_USER,
                    [user_email],
                    fail_silently=False,
                    )
                    return Response({'message':'check your email for instructions'},status=status.HTTP_200_OK)
                return Response({'message':'user does not exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
            except:
                return Response({'message':'user does not exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors)


class ResetPassword(generics.GenericAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def post(self,request,profile_slug,uidb64,token):
        user_id=urlsafe_base64_decode(uidb64).decode()
        try:
            user=User.objects.get(id=int(user_id))
            if PasswordResetTokenGenerator().check_token(user,token):
                new_password=request.data.get('new_password')
                confirm=request.data.get('confirm_password')
                if not new_password or not confirm:
                    return Response({'message':'Please enter new password'},status=status.HTTP_406_NOT_ACCEPTABLE)  
                if new_password==confirm:
                    user.set_password(new_password)
                    user.save()
                    return Response({'message':'password reset done'},status=status.HTTP_202_ACCEPTED)
                return Response({'message':'passwords do not match'},status=status.HTTP_406_NOT_ACCEPTABLE)
            return Response({'message':'Invalid Token'},status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
                return Response({'message':'user does not exist'},status=status.HTTP_404_NOT_FOUND)


# Profile owner get or update or delete his/her own profile
class Profile_change(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,profile_slug):
        user=self.request.user
        try:
            profile=Profile.objects.get(user=user,profile_slug=profile_slug)
            serializer=ProfileSerializer(profile)
            return Response(serializer.data,status=status.HTTP_200_OK) # put without json to avoid errors in postman
        except:
            return Response({'message':'user does not exist'},status=status.HTTP_404_NOT_FOUND)
    def put(self,request,profile_slug):
        user=self.request.user
        try:
            profile=Profile.objects.get(user=user,profile_slug=profile_slug)
            serializer=ProfileSerializer(profile,data=request.data)
            if serializer.is_valid():
                email_exists=Profile.objects.filter(email=serializer.validated_data['email']).exclude(user=user)
                if email_exists:
                    return Response({'message':'email is already used'},status=status.HTTP_226_IM_USED)
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK) # put without json to avoid errors in postman
            return Response(serializer.errors)
        except:
            return Response({'message':'you cant change this profile'},status=status.HTTP_403_FORBIDDEN)
    def delete(self,request,profile_slug):
        user=self.request.user
        try:
            profile=Profile.objects.get(user=user,profile_slug=profile_slug)
            profile.delete()
            user.delete()
            return Response({'message':'profile deleted'},status=status.HTTP_200_OK)
           
        except:
            return Response({'message':'you can not delete this profile'},status=status.HTTP_403_FORBIDDEN)
        
    
# Any user can view the profile 
class Profile_view(generics.RetrieveAPIView):
    permission_classes=[AllowAny]
    serializer_class=ProfileSerializer
    lookup_field='profile_slug'
    queryset=Profile.objects.all()


# profile owner creates post
class Posts_create(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self, request,profile_slug):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            title=request.data['title']
            file=request.FILES.get('file')
            description=request.data['description']
            try:
                profile=Profile.objects.get(user=self.request.user,profile_slug=profile_slug)
                Post.objects.create(profile=profile,title=title,description=description,file=file)
                json={'title':title,'description':description,'file':file}
                return Response(json,status=status.HTTP_201_CREATED)
            except:
                return Response({'message':'Can not create post on this profile'},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors)


# profile owner get or update or delete his/her post
class Post_change(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    lookup_field='post_slug'
    serializer_class=PostSerializer
    queryset=Post.objects.all()
    def get_object(self):
        queryset=self.get_queryset()
        try:
            profile=Profile.objects.get(user=self.request.user)
            return queryset.get(profile=profile,post_slug=self.kwargs['post_slug'])
        except:
            raise Http404('Can not change this post')

# Any user can view all posts related to profile
class Posts_list(generics.ListAPIView):
    permission_classes=[AllowAny]
    serializer_class=PostSerializer
    queryset=Post.objects.all()


# Any user can view single post related to profile
class Post_view(generics.RetrieveAPIView):
    permission_classes=[AllowAny]
    serializer_class=PostSerializer
    lookup_field='post_slug'
    queryset=Post.objects.all()



        












    
    
    
    
        
    
   

    
    

   




    