from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
    return render(request, 'todolist.html', {'welcome_text': "Welcome to your app"})