from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('', views.main, name='main'),

    path('task_list/', TaskList.as_view(), name='task_list'), 
    path('task_details/<int:pk>/', TaskDetails.as_view(), name='task_details'),
    path('task_add/', TaskAdd.as_view(), name='task_add'),
    path('task_details/edit/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task_details/<int:pk>/remove/', TaskDelete.as_view(), name='task_delete'),

    path('category_add/', CategoryAdd.as_view(), name='category_add'),
    path('category_list/', CategoryList.as_view(), name='category_list'),
    path('category_details/<int:pk>/', CategoryDetails.as_view(), name='category_details'),
    path('category_details/<int:pk>/remove/', CategoryDelete.as_view(), name='category_delete'),

    path('user_list/', UserList.as_view(), name='user_list'),
    path('user_details/<int:pk>/', UserDetails.as_view(), name='user_details'),    
    path('user_details/<int:pk>/remove/', UserDelete.as_view(), name='user_delete'),
]
