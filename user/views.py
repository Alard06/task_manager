from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.db.models import Q

from task.models import Profile
from user.forms import RegisterUserForm


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
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('index')


class ProfileLoginView(LoginView):
    model = User
    template_name = 'user/login.html'


def logout_view(request):
    logout(request)
    return redirect('index')
