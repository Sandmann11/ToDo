from django.shortcuts import render
from .models import Category, Task
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TaskForm, CategoryForm
from django.urls.base import reverse_lazy


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


class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_update.html' 


class TaskDelete(DeleteView):
    model = Task
    template_name = 'todo/task_delete.html'
    success_url = reverse_lazy('task_list')


class CategoryList(ListView):
    model = Category
    template_name = 'todo/category_list.html'


class CategoryDetails(DetailView):
    model = Category
    template_name = 'todo/category_details.html'


class CategoryAdd(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'todo/category_add.html'


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'todo/category_delete.html'
    success_url = reverse_lazy('category_list')


class UserList(ListView):
    model = User
    template_name = 'todo/user_list.html'


class UserDetails(DetailView):
    model = User
    template_name = 'todo/user_details.html'    


class UserDelete(DeleteView):
    model = User
    template_name = 'todo/user_delete.html'
    success_url = reverse_lazy('user_list')