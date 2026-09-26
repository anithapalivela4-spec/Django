from django.urls import path, include
from . import views
urlpatterns=[
    path('',views.emp_list,name='employee_list'),
]