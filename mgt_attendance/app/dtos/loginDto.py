from rest_framework import serializers

class LoginForm(serializers.Serializer):
    email = serializers.CharField()
    passWord = serializers.CharField()