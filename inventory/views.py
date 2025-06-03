from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch

from .models import Ingredient, IngredientDelivery
from .forms import IngredientForm, DeliveryForm


# ─── HTML  ▸ Ingredients ───────────────────────────────────────────────
def ingredient_list_view(request):
    ingredients = Ingredient.objects.order_by("name")
    return render(request, "inventory/list.html", {"ingredients": ingredients})


def ingredient_detail_view(request, pk):
    # 1) Prefetch — barcha IngredientDelivery obyektlarini oladi,
    #    keyin shablonda biz oxirgi 5 tasini ko‘rsatamiz.
    ingredient = get_object_or_404(
        Ingredient.objects.prefetch_related(
            Prefetch(
                "ingredientdelivery_set",
                queryset=IngredientDelivery.objects.select_related("created_by")
                                                  .order_by("-delivery_date")
            )
        ),
        pk=pk,
    )
    return render(request, "inventory/detail.html", {"ingredient": ingredient})


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_form.html"
    success_url = reverse_lazy("ingredient-list")


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_form.html"
    success_url = reverse_lazy("ingredient-list")


# ─── HTML  ▸ Deliveries ────────────────────────────────────────────────
def delivery_list_view(request):
    deliveries = (
        IngredientDelivery.objects
        .select_related("ingredient", "created_by")
        .order_by("-delivery_date")
    )
    return render(request, "inventory/deliveries_list.html", {"deliveries": deliveries})


class DeliveryCreateView(LoginRequiredMixin, CreateView):
    model = IngredientDelivery
    form_class = DeliveryForm
    template_name = "inventory/delivery_form.html"
    success_url = reverse_lazy("delivery-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
