from django.urls import path
from . import views

urlpatterns = [
    path("meals/",          views.MealListView.as_view(),   name="meal-list"),
    path("meals/new/",      views.MealCreateView.as_view(), name="meal-create"),
    path("meals/<int:pk>/", views.MealDetailView.as_view(), name="meal-detail"),

    path("served-meals/",      views.ServeListView.as_view(),  name="served-list"),
    path("served-meals/new/",  views.ServeCreateView.as_view(), name="serve-create"),
]
