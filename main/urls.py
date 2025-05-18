from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='taskList'),
    path('taskCreate/', views.taskCreate, name='taskCreate'),
    path('cartegoryCreate/', views.cartegoryCreate, name='cartegoryCreate'),
    path('cartegoryList/', views.cartegoryList, name='cartegoryList'),
]