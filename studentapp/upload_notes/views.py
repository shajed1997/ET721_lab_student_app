from django.shortcuts import render, redirect
from .models import NoteImage
from .forms import NoteImageForm

def note_list(request):
    notes = NoteImage.objects.all()
    return render(request, "upload_notes/note_list.html", {"notes": notes})

def add_note(request):
    if request.method == "POST":
        form = NoteImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteImageForm()
    return render(request, "upload_notes/add_note.html", {"form": form})
