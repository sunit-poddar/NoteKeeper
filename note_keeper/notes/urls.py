from django.urls import path
from notes import views

urlpatterns = [
    path("", views.index, name="index"),
    path('add/', views.add_note, name="new"),
    path('note/<int:note_id>/', views.note_details),
    path('edit/<int:note_id>/', views.edit, name='edit'),
    path('delete/<int:note_id>/', views.delete, name='delete'),
]
