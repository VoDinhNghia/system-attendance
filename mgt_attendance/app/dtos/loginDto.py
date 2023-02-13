from rest_framework import serializers

class LoginForm(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()