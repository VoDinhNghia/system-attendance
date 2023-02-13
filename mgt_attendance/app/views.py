# from django.shortcuts import render
from django.http import HttpResponse
from mongodb import connectDb

def index(request):
    db = connectDb()
    getAllUsers = db['users'].find({})
    for document in getAllUsers:
        print(document['email'])
        email = document['email']
        result = '<h1>Hello ' + email + ' and welcome to <u>Attendance App</u>!</h1>'
        return HttpResponse(result)
