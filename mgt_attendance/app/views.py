# from django.shortcuts import render
# from django.views.decorators.http import require_http_methods
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from app.dtos.loginDto import LoginForm
from app.services.user import findAllUsers

class Attendance(APIView):
    @swagger_auto_schema(request_body=LoginForm, tags=["Authors"])
    def post(self, request):
        serializer = LoginForm(data=request.data)
        if serializer.is_valid():
            json = serializer.data
            return Response(
                data={"status": "OK", "message": json, "statusCode": 200},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # permission_classes = (permissions.AllowAny)
    @swagger_auto_schema(tags=["Users"])
    def get(self, request):
        userLists = findAllUsers()
        print(type(userLists))
        return Response(
                data={"status": "OK", "message": "Get list users success.", "statusCode": 200, "data": userLists},
                status=status.HTTP_200_OK,
            )
