from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', )
        exclude = ('user', )


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
