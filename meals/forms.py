from django import forms
from .models import Meal, MealIngredient, ServedMeal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["name", "description"]
        widgets = {
            "name":        forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }

class MealIngredientForm(forms.ModelForm):
    class Meta:
        model = MealIngredient
        fields = ["ingredient", "quantity_required"]
        widgets = {
            "ingredient":        forms.Select(attrs={"class": "form-select"}),
            "quantity_required": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }

class ServeForm(forms.ModelForm):
    class Meta:
        model = ServedMeal
        fields = ["meal", "success"]
        widgets = {
            "meal":    forms.Select(attrs={"class": "form-select"}),
            "success": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
