# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello and welcome to <u>Attendance App</u>!</h1>")
