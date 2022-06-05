from . import views
from django.urls import path


urlpatterns = [
    path('<int:pk>', views.ProfileDetailView.as_view(), name='profile'),
    path('update/<int:pk>', views.ProfileUpdateView.as_view(), name='profile_update'),
]
