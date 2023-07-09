from django.urls import path
from .views import *

urlpatterns = [
    path('',TodoList.as_view(),name='todo_list'),
    path('create/',TodoCreate.as_view(),name="todo_create"),
    path('update/<int:pk>/',TodoUpdate.as_view(),name="todo_update"),
    path('delete/<int:pk>/',TodoDelete.as_view(),name="todo_delete")
]