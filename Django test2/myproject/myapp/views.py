from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello! Welcome to Home Page.")

def about(request):
    return HttpResponse("Welcome to About Page.")

def services(request):
    return HttpResponse("Welcome to Services Page.")

def contact(request):
    return HttpResponse("Welcome to Contact Page.")