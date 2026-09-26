from django.http import HttpResponse
from . models import course

# Create your views here.
def course_list(request):
    courses = course.objects.all()
    return HttpResponse(courses)
