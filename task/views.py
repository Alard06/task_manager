from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from task.forms import CreateTaskForm

from task.models import Task

# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        template = 'task/index.html'
        context = {'title': 'Менеджер задач'}
        return render(request, template, context)
    

class TaskListView(ListView):

    model = Task
    template_name='task/list_tasks.html'
    paginate_by = 10
    queryset = Task.objects.all()
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список задач'
        return context
    
    def get_ordering(self):
        ordering = self.request.GET.get('sort')
        sort_owner = self.request.GET.get('owner')
        if sort_owner:
            ordering = self.request.GET.get('owner')
        return ordering
    

class TaskDetailView(DetailView):

    model = Task
    template_name='task/detail_task.html'
  

def create_task(request):

    context = {}
    form = CreateTaskForm
    context = {'form': form}

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                Task.objects.create(
                    owner_id=request.user.id,
                    title=form.cleaned_data.get('title'),
                    description = form.cleaned_data.get('description'),
                    status = form.cleaned_data.get('status'),
                    published=form.cleaned_data.get('published'),
                    check = form.cleaned_data.get('check')
                )
                return redirect('tasks')
            else:
                return HttpResponse('Ошибка!')

    return render(request, 'task/create_task.html', context)