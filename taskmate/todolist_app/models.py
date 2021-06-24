from django.contrib.auth.models import User
from django.db import models
from django.db.models import manager
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        if (self.done == True):
            fin = "Done"
        else:
            fin = "Pending"

        return self.task + " - " + fin 
