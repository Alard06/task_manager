from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from task.forms import CreateTaskForm

from task.models import Task


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

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            try:
                object_list = Task.objects.filter(
                    Q(title=query) |
                    Q(owner__user__username=query) |
                    Q(pk=query))
            except ValueError:
                object_list = Task.objects.filter(
                    Q(title=query) |
                    Q(owner__user__username=query))
        else:
            object_list = Task.objects.all()
        return object_list


class TaskDetailView(DetailView):

    model = Task
    template_name = 'task/detail_task.html'


class TaskEditView(UpdateView):
    model = Task
    fields = ['owner', 'executor',
              'description', 'status',
              'published', 'check']
    template_name = 'task/edit_task.html'
    success_url = '/tasks'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task/confirm_delete.html'
    success_url = reverse_lazy('tasks')


class TaskProfileView(ListView):
    model = Task
    template_name = 'task/profile_task.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     context['obj_list'] = Task.objects.filter(pk=self.request.user.pk)
    #     return context


def create_task(request):

    form = CreateTaskForm
    context = {'form': form}

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                Task.objects.create(
                    owner_id=request.user.id,
                    title=form.cleaned_data.get('title'),
                    description=form.cleaned_data.get('description'),
                    status=form.cleaned_data.get('status'),
                    published=form.cleaned_data.get('published'),
                    check=form.cleaned_data.get('check')
                )
                return redirect('tasks')
            else:
                return HttpResponse('Ошибка!')

    return render(request, 'task/create_task.html', context)