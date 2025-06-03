from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch

from .models import Meal, MealIngredient, ServedMeal
from .forms import MealForm, ServeForm


# ─── HTML  ▸  Meals ────────────────────────────────────────────────────
class MealListView(ListView):
    model = Meal
    template_name = "meals/list.html"
    context_object_name = "meals"
    ordering = ["name"]


class MealDetailView(DetailView):
    model = Meal
    template_name = "meals/detail.html"
    context_object_name = "meal"

    def get_queryset(self):
        return Meal.objects.prefetch_related(
            Prefetch(
                "mealingredient_set",
                queryset=MealIngredient.objects.select_related("ingredient"),
            )
        )


class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealForm
    template_name = "meals/meal_form.html"
    success_url = reverse_lazy("meal-list")


# ─── HTML  ▸  Served Meals ─────────────────────────────────────────────
class ServeListView(ListView):
    model = ServedMeal
    template_name = "meals/served_list.html"
    context_object_name = "served_meals"
    ordering = ["-served_at"]
    paginate_by = 10


class ServeCreateView(LoginRequiredMixin, CreateView):
    model = ServedMeal
    form_class = ServeForm
    template_name = "meals/serve_form.html"
    success_url = reverse_lazy("served-list")

    def form_valid(self, form):
        form.instance.served_by = self.request.user
        return super().form_valid(form)
