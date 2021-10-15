from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'new.html'
    fields = ['title', 'description', 'completed']

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    fields = ['title', 'description', 'completed']

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class TaskCompletedListView(ListView):
    model = Task
    template_name = 'completed.html'

class TaskIncompletedListView(ListView):
    model = Task
    template_name = 'incompleted.html'

class TaskWarningView(TemplateView):
    model = Task
    template_name = 'warning.html'