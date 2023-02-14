from rest_framework import status
from rest_framework.response import Response
import requests

def login(serializer, request):
    if serializer.is_valid():
        body = serializer.data
        resultLogin = requests.post('http://localhost:3000/auth/login', data=body)
        results = resultLogin.json()
        if results['statusCode'] == 200:
            data = results['data']
            request.session['accessToken'] = data['accessToken']
            request.session['email'] = data['email']
            request.session['_id'] = data['_id']
        return Response(
            data=results,
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)