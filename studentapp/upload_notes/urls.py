from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),  # Note list page
    path('add/', views.add_note, name='add_note'),  # Add new note page
]
