from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import NoteForm
from .models import Note
from .forms import UserRegisterForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


@login_required()
def note_list(request, *args, **kwargs):
    notes = Note.objects.all()

    context = {'notes': notes}
    return render(request, 'note_home.html', context)


def note_details(request, note_id):
    note = Note.objects.get(id=note_id)
    form = NoteForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Note modified!")

    context = {'note': note}

    return render(request, 'note_details.html', context)


@login_required
def add_note(request, *args, **kwargs):
    form = NoteForm(request.POST or None)

    if form.is_valid():
        stock = form.save(commit=False)
        stock.author = request.user
        stock.save()
        messages.success(request, "Note created!")
        return redirect('index')

    context = {'form': form}

    return render(request, 'add_note.html', context)


@login_required
def edit(request, note_id):
    obj = Note.objects.get(id=note_id)
    if request.user == obj.author:
        if request.method == 'POST':
            form = NoteForm(request.POST, instance=obj)
            if form.is_valid():
                stock = form.save(commit=False)
                stock.author = request.user
                stock.save()
                messages.success(request, f'Note Edited!')
                return redirect('index')
        else:
            form = NoteForm(instance=obj)
        return render(request, 'edit_note.html', {'form': form})
    return redirect('index')


@login_required
def delete(request, note_id):
    obj = Note.objects.get(id=note_id)
    if request.user == obj.author:
        Note.objects.filter(id=note_id).delete()
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
