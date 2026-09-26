
from django.http import HttpResponse
from . models import student, faculty, course, department

# Create your views here.
def student_list(request):
    students = student.objects.all()
    return HttpResponse(students)

def faculty_list(request):
    faculties = faculty.objects.all()
    return HttpResponse(faculties)

def course_list(request):
    courses = course.objects.all()
    return HttpResponse(courses)

def department_list(request):
    departments = department.objects.all()
    return HttpResponse(departments)