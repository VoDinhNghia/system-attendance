from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from app.dtos.loginDto import LoginForm
from drf_yasg import openapi
from app.controllers.auth import login
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import action, api_view

class AuthView(APIView):
    @swagger_auto_schema(request_body=LoginForm, operation_description="Api Login Service")
    def post(self, request):
        serializer = LoginForm(data=request.data)
        result = login(serializer, request)
        return result
    
    @swagger_auto_schema(operation_description="Api Logout Service")
    def put(self, request):
        return Response(
                data={"status": "OK", "message": "Logout success.", "statusCode": 200, "data": 'ok'},
                status=status.HTTP_200_OK,
            )
    
    @swagger_auto_schema(operation_description="Api get me info")
    def get(self, request):
        print('accessToken', request.session['accessToken'])
        print('email', request.session['email'])
        print('id', request.session['_id'])
        return Response(
                data={"status": "OK", "message": "Get list users success.", "statusCode": 200, "data": 'ok'},
                status=status.HTTP_200_OK,
            )
