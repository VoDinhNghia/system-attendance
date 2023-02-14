from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from app.dtos.loginDto import LoginForm
from app.controllers.auth import login
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view

class UserView(APIView):
    @swagger_auto_schema(operation_description="Api get users")
    def get(self, request):
        print('hee', request)
        return Response(
                data={"status": "OK", "message": "Get list users success.", "statusCode": 200, "data": 'ok'},
                status=status.HTTP_200_OK,
            )
    
    @swagger_auto_schema(operation_description="Api get user by id")
    def get(self, request):
        return Response(
                data={"status": "OK1", "message": "Get list users success.", "statusCode": 200, "data": 'ok'},
                status=status.HTTP_200_OK,
            )
