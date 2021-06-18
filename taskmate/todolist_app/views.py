from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def todolist(request):
    context = {'welcome_text': "Welcome to your app"}
    return render(request, 'todolist.html', context)



def contact(request):
    context = {'welcome_text': "Contact Us"}
    return render(request, 'contact.html', context)



def about(request):
    context = {'welcome_text': "About Us"}
    return render(request, 'about.html', context)