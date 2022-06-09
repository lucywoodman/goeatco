from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db import transaction
from .forms import ProfileUpdateForm, UserUpdateForm
from .models import Profile


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Class for the profile detail page
    """
    model = Profile

    def get_object(self, *args, **kwargs):
        """
        Ensures that the logged in user can only see their own profile
        """
        return self.request.user.profile


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    Class for the profile update form page
    """
    model = Profile
    form_class = UserUpdateForm
    second_form_class = ProfileUpdateForm
    template_name = 'profiles/profile_form.html'

    def get_object(self, *args, **kwargs):
        """
        Ensures that the logged in user can only see their own profile
        """
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        """
        Handles the form context
        """
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
        """
        Handle form validation
        """
        context = self.get_context_data()
        user_form = context['user_form']
        profile_form = context['profile_form']
        with transaction.atomic():
            if user_form.is_valid() and profile_form.is_valid():
                user_form.instance = self.request.user
                profile_form.instance = self.object
                user_form.save()
                profile_form.save()
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile')
