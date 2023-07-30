from django.shortcuts import render
from django.views import View

# Create your views here.

class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        template = 'task/index.html'
        context = {'title': 'Менеджер задач'}
        return render(request, template, context)