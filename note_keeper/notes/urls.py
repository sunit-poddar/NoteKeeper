from django.urls import path
from notes import views

urlpatterns = [
    path("", views.index, name="index"),
    path('add/', views.add_note, name="new"),
    path('note/<note_slug>/', views.note_details, name="note"),
    path('edit/<int:note_id>/', views.edit, name='edit'),
    path('delete/<int:note_id>/', views.delete, name='delete'),
    path('publish/<int:note_id>', views.publish, name='publish')
]
