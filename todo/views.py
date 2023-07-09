from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm
# Create your views here.
"""
def home(request):
    return render(request, 'home.html')
"""
class TodoList(ListView):
    model = Todo

class TodoCreate(SuccessMessageMixin,CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    success_message = "Todo Successfully Created"

class TodoUpdate(SuccessMessageMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    success_message = "Todo Successfully Updated!"

class TodoDelete(SuccessMessageMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')
    success_message = "Deleted Todo Successfully!!"


