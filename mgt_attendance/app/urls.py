from django.urls import path

from . import views

urlpatterns = [
    path('', views.Attendance.as_view(), name='login'),           
]