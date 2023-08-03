from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from django.db.models import Q

from task.models import Profile

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

    

    