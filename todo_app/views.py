from todo_app.forms import TaskForm
from django.shortcuts import render
from .models import Task, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import requests


def admin(request):
    return render(request, '', {})


def main(request):
    return render(request, 'todo/main.html', {})


class TaskList(ListView):
    model = Task
    template_name = 'todo/task_list.html'


class TaskDetails(DetailView):
    model = Task
    template_name = 'todo/task_details.html'


class TaskAdd(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_add.html'