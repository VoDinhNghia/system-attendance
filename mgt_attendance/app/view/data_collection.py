from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from app.dtos.collection_data import CollectionImageForm
from drf_yasg import openapi
from app.controllers.auth import login
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import action, api_view

class DataCollectionView(APIView):
    @swagger_auto_schema(request_body=CollectionImageForm, operation_description="Api add image into folder to trainning model")
    def post(self, request):
        return Response(
                data={"status": "OK", "message": "Collection images data success.", "statusCode": 200, "data": 'ok'},
                status=status.HTTP_200_OK,
            )
