from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProfileDetailView.as_view(), name='profile'),
    path('update', views.ProfileUpdateView.as_view(), name='profile_update'),
]
