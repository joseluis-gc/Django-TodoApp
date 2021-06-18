from django import forms
from django.db.models import fields
from todolist_app.models import TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = [
            'task', 
            'done'
        ]
