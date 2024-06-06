from .models import Offer
def offers_context(request):
    offers=Offer.objects.all().filter(is_active=True)

    return {'offers':offers}
    