from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView
from django.db.models import Q
from django.views.generic.edit import FormMixin

from task.models import Profile
from user.forms import RegisterUserForm, UpdateCheckEmail


class ProfileView(FormMixin, DetailView):
    model = Profile
    template_name = 'user/profile.html'
    form_class = UpdateCheckEmail

    def get_success_url(self):
        return reverse('profile_view', kwargs={'pk': self.object.pk})
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            check_email = form.cleaned_data['check_email']
            p = Profile.objects.get(pk=request.user.pk)
            p.check_email = check_email
            p.save()
            print(p.check_email)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


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
