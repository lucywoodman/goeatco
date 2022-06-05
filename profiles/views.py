from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ProfileForm
from .models import Profile


class ProfileDetailView(generic.DetailView):
    model = Profile


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
