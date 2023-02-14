from django.urls import path

from . import views
from app.view.auth import AuthView
from app.view.user import UserView

urlpatterns = [
    path('api/auth/', AuthView.as_view(), name='auth_route'),
    path('api/users/', UserView.as_view(), name='user_route'),     
]