from django.contrib import admin

# Register your models here.
from . models import student, faculty, course, department
admin.site.register(student)
admin.site.register(faculty)
admin.site.register(course)
admin.site.register(department)
