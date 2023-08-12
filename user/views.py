from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.db.models import Q

from task.models import Profile
from user.forms import UserCreateForm


class ProfileView(DetailView):
    model = Profile
    template_name = 'user/profile.html'


class ProfileListView(ListView):
    model = Profile
    template_name = 'user/profile_list.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Profile.objects.filter(
                Q(user__username__icontains=query) | 
                Q(user__last_name__icontains=query) |
                Q(user__email__icontains=query))
        else:
            object_list = Profile.objects.all()

        return object_list


class ProfileCreateView(CreateView):
    model = User
    template_name = 'user/register.html'
    fields = ['username', '2']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('index')



def profile_login(request):
    return render(request, 'user/login.html')
