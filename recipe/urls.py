from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe_list'),
    path('add', views.RecipeAddView.as_view(), name='recipe_add'),
    path('<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
]
