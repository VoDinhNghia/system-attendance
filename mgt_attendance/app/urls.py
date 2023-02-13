from django.urls import path

from . import views

urlpatterns = [
    path('', views.Attendance.index, name='index'),
    path('login/', views.Attendance.as_view(), name='login'),           
]