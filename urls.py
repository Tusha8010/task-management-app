from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('status/<int:id>/', views.update_status, name='update_status'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),

]
