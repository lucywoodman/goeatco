from . import views
from django.urls import path


urlpatterns = [
    path(
        '',
        views.HomeListView.as_view(),
        name='home'),
    path(
        'cookbook',
        views.CookbookView.as_view(),
        name='cookbook'),
    path(
        'recipe/create',
        views.RecipeCreateView.as_view(),
        name='recipe_create'),
    path(
        'recipe/<slug:slug>/update',
        views.RecipeUpdateView.as_view(),
        name='recipe_update'),
    path(
        'recipe/<slug:slug>/delete',
        views.RecipeDeleteView.as_view(),
        name='recipe_delete'),
    path(
        'recipe/<slug:slug>/',
        views.RecipeDetailView.as_view(),
        name='recipe_detail'),
    path(
        'recipe/save/<slug:slug>',
        views.RecipeSave,
        name='recipe_save'),
]
