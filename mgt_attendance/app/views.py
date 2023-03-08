# from django.shortcuts import render
# from django.views.decorators.http import require_http_methods
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from app.dtos.loginDto import LoginForm
from app.services.user import findAllUsers, findOneUser
import requests
from app.controllers.auth import login

class Attendance(APIView):
    def view():
        print('view')
