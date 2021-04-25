from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import requests

def main(request):
    return render(request, 'todo/main.html', {}) 