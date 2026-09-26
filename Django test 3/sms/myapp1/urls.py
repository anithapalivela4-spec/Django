from django.urls import path, include
from . import views
urlpatterns=[
    path('',views.student_list,name='student_list'),
    path('',views.faculty_list,name='faculty_list'),
    path('',views.course_list,name='course_list'),
    path('',views.department_list,name='department_list'),
]