from .views import RecipeList, RecipeAdd, RecipeDetail
from django.urls import path


urlpatterns = [
    path('', RecipeList.as_view(), name='recipe_list'),
    path('add', RecipeAdd.as_view(), name='recipe_add'),
    path('<slug:slug>/', RecipeDetail.as_view(), name='recipe_detail'),
]
