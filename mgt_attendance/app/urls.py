from django.urls import path

from . import views
from app.view.data_collection import DataCollectionView
from app.view.user import UserView

urlpatterns = [
    path('api/data-collection/', DataCollectionView.as_view(), name='data_collection_route'),
    path('api/users/', UserView.as_view(), name='user_route'),     
]