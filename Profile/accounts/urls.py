from django.urls import path, reverse_lazy
from . import views
from . import api
# email verify imports
from django.contrib.auth import views as auth_views


app_name='accounts'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login-view/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout'),
    path('profile-view/',views.profile,name='profile'),
    path('edit-profile/',views.edit_profile,name='edit_profile'),
    path('upload-post/',views.upload_post,name='upload_post'),
    #activate account sent by signup
    path('activate/<uidb64>/<token>/',views.Activate_account,name='activate'),
    #reset password urls
    path('reset-email/',views.Reset_Email,name='reset_email'),
    path('reset_password/<str:uidb64>/<str:token>/',views.Reset_password,name='reset_password'),
    #Api urls
    path('api-signup/',api.Signup.as_view(),name='api_signup'),
    path('api-activate/<str:uidb64>/<str:token>/',api.ActivateAccount.as_view(),name='api-activate'),
    path('api-login/',api.Login.as_view(),name='api_login'),
    path('api-logout/',api.Logout.as_view(),name='api_logout'),
    #Api reset password urls
    path('<str:profile_slug>/api-changepassword/',api.ChangeUserPassword.as_view(),name='change_pass'),
    path('<str:profile_slug>/reset-email/',api.RequestPasswordResetEmail.as_view(),name='reset_email'),
    path('<str:profile_slug>/request_password/<str:uidb64>/<str:token>/',api.ResetPassword.as_view(),name='request_password'),
    #Api profile urls
    path('<str:profile_slug>/view/',api.Profile_view.as_view(),name='view_profile'),
    path('<str:profile_slug>/update/',api.Profile_change.as_view(),name='update_profile'),
    #Api posts urls 
    path('<str:profile_slug>/create-post/',api.Posts_create.as_view(),name='create_post'),
    path('<str:profile_slug>/posts-list/',api.Posts_list.as_view(),name='posts_list'),
    path('<str:profile_slug>/<str:post_slug>/post-detail/',api.Post_change.as_view(),name='post_detail'),
    path('<str:profile_slug>/<str:post_slug>/post-view/',api.Post_view.as_view(),name='post_view'),
    ]


    # Alternative method using django forms for reset password for future refrence
    
    #path('verify/',auth_views.PasswordResetView.as_view(template_name='accounts/email_verify.html',success_url=reverse_lazy('accounts:password_reset_done')),name='verify'),
    #path('reset-password-sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/instructions.html'),name='password_reset_done'),
    #path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_password.html',success_url=reverse_lazy('accounts:password_reset_complete')),name='password_reset_confirm'),
    #path('reset-password-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_done.html'),name='password_reset_complete'),
    
    