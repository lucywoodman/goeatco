from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.db import transaction
from .forms import ProfileUpdateForm, UserUpdateForm
from .models import Profile


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = UserUpdateForm
    second_form_class = ProfileUpdateForm
    template_name = 'profiles/profile_form.html'
    pk = None

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = self.form_class(
                self.request.POST, instance=self.request.user)
            context['profile_form'] = self.second_form_class(
                self.request.POST, instance=self.object)
        else:
            context['user_form'] = self.form_class(instance=self.request.user)
            context['profile_form'] = self.second_form_class(
                instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        profile_form = context['profile_form']
        self.pk = self.request.user.id
        with transaction.atomic():
            if user_form.is_valid() and profile_form.is_valid():
                user_form.instance = self.request.user
                profile_form.instance = self.object
                user_form.save()
                profile_form.save()
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        print(self.pk)
        return reverse('profile', kwargs={'pk': self.pk})
