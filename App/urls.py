from typing import Hashable
from django.urls import path
from .views import Home, Update, Delete



urlpatterns = [
    path('',Home, name='Home'),
    path('update/<int:task_id>/',Update, name='Update'),
    path('delete/<int:task_id>/',Delete, name='Delete'),

]
