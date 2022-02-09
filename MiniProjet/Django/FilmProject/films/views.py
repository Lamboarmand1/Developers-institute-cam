from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Film
from .forms import *

# Create your views here.
def home(request):
    all_films = Film.objects.all()
    return render(request, 'homepage.html', {'films':all_films})

def addfilm(request):
    if request.method == 'POST':
        form = AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Film succesfully added to the database')
            return redirect('home')
    else:
        fill_form = AddFilmForm()
        return render(request, 'addfilm.html', {'form':fill_form})

def addDirector(request):
    if request.method=='POST':
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            new_director = form.save()
            messages.success(request, f'Director {new_director.first_name} succesfully added to the database')
            return redirect('home')
    else:
        dir_form = AddDirectorForm()
        return render(request, 'addDirector.html', {'form':dir_form})
