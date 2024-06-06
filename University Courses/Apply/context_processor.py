from .models import Profile,Application

def profile_context(request,profile=None):
    if request.user.is_authenticated:
        profile=Profile.objects.get(user=request.user)
    return {'profile':profile}

