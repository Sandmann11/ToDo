from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('', views.main, name='main'),
    path('task_list/', TaskList.as_view(), name='task_list'), 
    path('task_details/<int:pk>/', TaskDetails.as_view(), name='task_details'),
    path('task_add/', TaskAdd.as_view(), name='task_add'),
    path('category_add/', CategoryAdd.as_view(), name='category_add'),
]
