from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_watches, name='watches'),
    path('<int:watch_id>/', views.watch_detail, name='watch_detail'),
    path('add/', views.add_watch, name='add_watch'),
    path('edit/<int:watch_id>/', views.edit_watch, name='edit_watch'),
]
