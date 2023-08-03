from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from task.models import Profile

class ProfileView(DetailView):

    model = Profile
    template_name = 'user/profile.html'

class ProfileListView(ListView):

    model = Profile
    template_name = 'user/profile_list.html'


    