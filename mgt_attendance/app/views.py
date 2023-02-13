# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from mongodb import connectDb
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from app.dtos.loginDto import LoginForm

class Attendance(APIView):
    @require_http_methods(["GET"])
    def index(request):
        db = connectDb()
        getAllUsers = db['users'].find({})
        for document in getAllUsers:
            print(request)
            print(document['email'])
            email = document['email']
            result = '<h1>Hello ' + email + ' and welcome to <u>Attendance App</u>!</h1>'
            return HttpResponse(result)
    
    # permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(request_body=LoginForm)
    def post(self, request):
        serializer = LoginForm(data=request.data)
        if serializer.is_valid():
            json = serializer.data
            return Response(
                data={"status": "OK", "message": json},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
