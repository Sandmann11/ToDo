from django import forms
from django.forms import ModelForm
from .models import Task, Category


choices = Category.objects.all().values_list('name', 'name')


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['author', 'name', 'description', 'details', 'category', 'priority', 'date_due']

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'date_due': forms.TextInput(attrs={'class': 'form-control'}),
            # 'reminder': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }