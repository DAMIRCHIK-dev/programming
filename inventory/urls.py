from django.urls import path
from . import views

urlpatterns = [
    # Ingredient CRUD
    path("view/", views.ingredient_list_view, name="ingredient-list"),
    path("",      views.ingredient_list_view, name="ingredient-list-root"),  # alias
    path("ingredient/<int:pk>/",       views.ingredient_detail_view, name="ingredient-detail"),
    path("ingredient/new/",            views.IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredient/<int:pk>/edit/",  views.IngredientUpdateView.as_view(), name="ingredient-update"),

    # Deliveries
    path("deliveries/",      views.delivery_list_view, name="delivery-list"),
    path("deliveries/new/",  views.DeliveryCreateView.as_view(), name="delivery-create"),
]
