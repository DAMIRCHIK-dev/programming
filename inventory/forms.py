from django import forms
from .models import Ingredient, IngredientDelivery


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name", "quantity", "min_quantity"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "min_quantity": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = IngredientDelivery
        fields = ["ingredient", "quantity", "delivery_date"]
        widgets = {
            "ingredient": forms.Select(attrs={"class": "form-select"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "delivery_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }
