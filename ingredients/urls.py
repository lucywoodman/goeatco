from . import views
from django.urls import path

urlpatterns = [
    path('', views.IngredientListView.as_view(), name='ingredient_list'),
    path('create', views.IngredientCreateView.as_view(),
         name='ingredient_create'),
    path('update/<int:pk>/',
         views.IngredientUpdateView.as_view(), name='ingredient_update'),
    path('delete/<int:pk>/',
         views.IngredientDeleteView.as_view(), name='ingredient_delete'),
]
