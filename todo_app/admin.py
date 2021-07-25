from django.contrib import admin
from .models import Task, Category


# admin.site.register(Task)
admin.site.register(Category)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'category')
    list_filter = ('id', 'author', 'category')
    search_fields = ('name', 'description', 'details')