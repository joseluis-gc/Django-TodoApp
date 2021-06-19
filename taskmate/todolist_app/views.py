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


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    messages.success(request,('Task Deleted successfully.'))
    return redirect('todolist')



def edit_task(request, task_id):
    if(request.method == "POST"):
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if(form.is_valid()):
            form.save()

        messages.success(request,('Task Updated.'))
        return redirect('todolist')    
    else:
        task_object = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_object':task_object})    


def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    messages.success(request,('Task Marked As Complete.'))
    return redirect('todolist')


def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    messages.success(request,('Task Marked As Pending.'))
    return redirect('todolist')




def contact(request):
    context = {'welcome_text': "Contact Us"}
    return render(request, 'contact.html', context)



def about(request):
    context = {'welcome_text': "About Us"}
    return render(request, 'about.html', context)