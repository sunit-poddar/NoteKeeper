from django.shortcuts import render

from .forms import NoteForm
from .models import Note


# Create your views here.

def note_list(request, *args, **kwargs):
    notes = Note.objects.all()

    context = {'notes': notes}
    return render(request, 'note_home.html', context)


def note_details(request, note_id):
    note = Note.objects.get(id=note_id)

    context = {'note': note}

    return render(request, 'note_details.html', context)


def add_note(request, *args, **kwargs):
    form = NoteForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = NoteForm()

    context = {'form': form}

    return render(request, 'add_note.html', context)
