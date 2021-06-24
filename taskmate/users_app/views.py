from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegisterForm
from django.contrib import messages


# Create your views here.
def register(request):
    #return HttpResponse('Uses App Working.')

    if(request.method == "POST"):
        register_form = CustomRegisterForm(request.POST)
        if(register_form.is_valid()):
            register_form.save()
            messages.success(request, ("Account created successfully!"))
            return redirect('register')

    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})
    
