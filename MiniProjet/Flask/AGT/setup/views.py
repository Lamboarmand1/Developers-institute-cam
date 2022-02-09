from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormTask
# Create your views here.
from .models import Task


def index(request):
    form = FormTask(request.POST or None)
    if form.is_valid():
        form.save()
    list = Task.objects.all()
    context = {'form': form,'taches':list}
    return render(request, 'index.html',context)

def update(request, my_id):
    obj = get_object_or_404(Task, id=my_id)
    form = FormTask(request.POST  or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form':form})

def delete(request, my_id):
    obj = get_object_or_404(Task, id=my_id)
    obj.delete()
    return redirect('/')
