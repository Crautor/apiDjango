from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('user/', views.getUsers, name='getAll'),
    path('user/ids', views.getUsersWithId, name='getAllWithID'),
    path('user/<int:id>', views.getByID, name='getByID'),
    path('user/departament/<str:departament>', views.getByDepartament, name='getByDepartament'),
    path('user/create/', views.createUser, name='createUser'),
    path('user/update/<int:id>', views.updateUser, name='updateUser'),
    path('user/delete/<int:id>', views.deleteUser, name='deleteUser'),
]

