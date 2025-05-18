from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='taskList'),
    path('taskCreate/', views.taskCreate, name='taskCreate'),
    path('cartegoryCreate/', views.cartegoryCreate, name='cartegoryCreate'),
    path('cartegoryList/', views.cartegoryList, name='cartegoryList'),
    path('editTask/<int:id>/', views.editTask, name='editTask'),
    path('editCategory/<int:id>/', views.editCategory, name='editCategory'),
    path('deleteTask/<int:id>/', views.deleteTask, name='deleteTask'),
    path('deleteCategory/<int:id>/', views.deleteCategory, name='deleteCategory'),
]