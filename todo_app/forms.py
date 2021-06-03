from django import forms
from .models import Task, Category

# choices = Category.objects.all().values_list('name', 'name')

# print(choices)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'details', 'category', 'priority', 'date_due', 'reminder']

        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'decription': forms.Textarea(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
            # 'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'priority': forms.TextInput(attrs={'class': 'form-control'}),
            'date_due': forms.TextInput(attrs={'class': 'form-control'}),
            'reminder': forms.TextInput(attrs={'class': 'form-control'}),
        }