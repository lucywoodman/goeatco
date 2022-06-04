from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('cookbook', views.CookbookView.as_view(), name='cookbook'),
    path('recipe/create', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<slug:slug>/update',
         views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<slug:slug>/delete',
         views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('recipe/<slug:slug>/',
         views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/save/<slug:slug>', views.RecipeSave, name='recipe_save'),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/create', views.IngredientCreateView.as_view(),
         name='ingredient_create'),
    path('ingredients/update/<int:pk>/',
         views.IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredients/delete/<int:pk>/',
         views.IngredientDeleteView.as_view(), name='ingredient_delete'),
]
