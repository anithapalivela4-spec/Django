from django.http import HttpResponse
from . models import product

# Create your views here.
def product_list(request):
    products = product.objects.all()
    return HttpResponse(products)