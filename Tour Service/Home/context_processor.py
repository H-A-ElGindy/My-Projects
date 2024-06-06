from Services.models import Category,Continent

def categories(request):
    category=Category.objects.all()
    return {'category':category}

