from django.contrib import admin
from .models import Task, Category


# admin.site.register(Task)
admin.site.register(Category)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_due', 'priority', 'category', 'date_created', 'author')
    list_filter = ('author', 'priority', 'date_due')
    search_fields = ('name', 'description', 'details', 'category')
    date_hierarchy = 'date_created'
    ordering = ('date_due', 'priority', 'category')