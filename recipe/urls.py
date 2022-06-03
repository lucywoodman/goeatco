from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('add', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('<slug:slug>/update', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('<slug:slug>/delete', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
]
