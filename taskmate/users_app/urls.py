from django.urls import path
#from todolist_app import views
from users_app import views


urlpatterns = [
    path('register', views.register, name='register'),
    
    
]
