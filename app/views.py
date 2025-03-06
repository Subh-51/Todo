from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
     all_todos = Todo.objects.all()
     d = {'all_todos': all_todos}
     if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        TO = Todo(title=title, desc=desc)
        TO.save()
     return render(request,'home.html',d)
def update(request, pk):
    T = Todo.objects.get(pk=pk)
    d = {'T': T}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        T.title = title
        T.desc = desc
        T.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'update.html', d)

