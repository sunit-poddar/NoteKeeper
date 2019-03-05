from django.shortcuts import render
from django.template import loader

from .forms import NoteForm
from .models import Note


# Create your views here.

def home(request):
    notes = Note.objects.all()

    template = loader.get_template('note.html')
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    context = {'notes': notes, 'form': form}
    return render(request, 'note.html', context)
