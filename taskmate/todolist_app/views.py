from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.add_task_form import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def todolist(request):

    if(request.method == "POST" or None):
        form = TaskForm(request.POST)
        if(form.is_valid()):
            instance = form.save(commit=False)
            instance.owner = request.user
            #form.save()
            instance.save()
            messages.success(request,('New Task Added.'))
        else:
            messages.success(request,('Invalid Data, Please Try Again.'))
        return redirect('todolist')    
    else:
        #all_tasks = TaskList.objects.all
        all_tasks = TaskList.objects.filter(owner = request.user)
        return render(request, 'todolist.html', {'all_tasks':all_tasks})    

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if(task.owner == request.user):
        task.delete()
        messages.success(request,('Task Deleted successfully.'))
    else:
        messages.success(request,('Access denied.'))
        
    return redirect('todolist')


@login_required
def edit_task(request, task_id):
    if(request.method == "POST"):
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if(form.is_valid()):
            form.save()
            messages.success(request,('Task Updated.'))
        else:    
            messages.success(request,('Invalid Data, Please Try Again.'))
        return redirect('todolist')    
    else:
        task_object = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_object':task_object})    

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)

    if(task.owner == request.user):
        task.done = True
        task.save()
        messages.success(request,('Task Marked As Complete.'))
    else:
        messages.success(request,('Access denied.'))
    
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if(task.owner == request.user):
        task.done = False
        task.save()
        messages.success(request,('Task Marked As Pending.'))
    else:        
        messages.success(request,('Access denied.'))
        
    return redirect('todolist')




def contact(request):
    context = {'welcome_text': "Contact Us"}
    return render(request, 'contact.html', context)



def about(request):
    context = {'welcome_text': "About Us"}
    return render(request, 'about.html', context)


    
def index(request):
    context = {'welcome_text': "Index"}
    return render(request, 'index.html', context)