from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('admin/', views.admin, name='admin'),
    path('', views.main, name='main'),
]
