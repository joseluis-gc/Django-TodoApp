from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.add_task_form import TaskForm
from django.contrib import messages


# Create your views here.
def todolist(request):

    if(request.method == "POST" or None):
        form = TaskForm(request.POST)
        if(form.is_valid()):
            form.save()
        messages.success(request,('New Task Added.'))
        return redirect('todolist')    
    else:
        all_tasks = TaskList.objects.all
        return render(request, 'todolist.html', {'all_tasks':all_tasks})    



def contact(request):
    context = {'welcome_text': "Contact Us"}
    return render(request, 'contact.html', context)



def about(request):
    context = {'welcome_text': "About Us"}
    return render(request, 'about.html', context)