# from django.shortcuts import render
# from django.views.decorators.http import require_http_methods
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from app.dtos.loginDto import LoginForm
from app.services.user import findAllUsers, findOneUser
import requests

class Attendance(APIView):
    @swagger_auto_schema(request_body=LoginForm, tags=["Authors"])
    def post(self, request):
        serializer = LoginForm(data=request.data)
        if serializer.is_valid():
            body = serializer.data
            resultLogin = requests.post('http://localhost:3000/auth/login', data=body)
            results = resultLogin.json()
            if results['statusCode'] == 200:
                data = results['data']
                request.session['accessToken'] = data['accessToken']
                request.session['email'] = data['email']
                request.session['_id'] = data['_id']
                print('accessToken', request.session['accessToken'])
            return Response(
                data=results,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # permission_classes = (permissions.AllowAny)
    @swagger_auto_schema(tags=["Users"])
    def get(self, request):
        userLists = findAllUsers()
        print('accessToken', request.session['accessToken'])
        print('email', request.session['email'])
        return Response(
                data={"status": "OK", "message": "Get list users success.", "statusCode": 200, "data": userLists},
                status=status.HTTP_200_OK,
            )
