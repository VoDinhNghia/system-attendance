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
    @swagger_auto_schema(request_body=LoginForm, tags=["Auth"])
    def post(self, request):
        serializer = LoginForm(data=request.data)
        result = login(serializer, request)
        return result

    permission_classes = (permissions.AllowAny)
    @swagger_auto_schema(tags=["Users"])
    def get(self, request):
        userLists = findAllUsers()
        print('accessToken', request.session['accessToken'])
        print('email', request.session['email'])
        print('id', request.session['_id'])
        return Response(
            data={"status": "OK", "message": "Get list users success.", "statusCode": 200, "data": userLists},
            status=status.HTTP_200_OK,
        )
