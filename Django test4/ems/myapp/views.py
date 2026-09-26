from django.http import HttpResponse
from . models import employee

# Create your views here.
def emp_list(request):
    employees = employee.objects.all()
    return HttpResponse(employees)

