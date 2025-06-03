# tests/test_models.py
import pytest
from inventory.models import Ingredient
from meals.models import Meal, MealIngredient, ServedMeal

pytestmark = pytest.mark.django_db

def make_ingredient(name="Flour", qty=1000, min_qty=100):
    return Ingredient.objects.create(name=name, quantity=qty, min_quantity=min_qty)

def test_ingredient_str():
    ing = make_ingredient()
    assert str(ing) == "Flour"

def test_ingredient_low_stock_property():
    ing = make_ingredient(qty=50, min_qty=100)
    assert ing.quantity < ing.min_quantity

def test_servedmeal_defaults():
    meal = Meal.objects.create(name="Porridge")
    served = ServedMeal.objects.create(meal=meal)
    assert served.success is True
