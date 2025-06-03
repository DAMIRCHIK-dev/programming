# inventory/factories.py
from abc import ABC, abstractmethod
from inventory.models import Ingredient, IngredientType

class IngredientFactory(ABC):
    @abstractmethod
    def create(self, name, **extras):
        ...

class FruitFactory(IngredientFactory):
    def create(self, name, **extras):
        defaults = dict(calories=60, fats=0.2, carbs=15)
        return Ingredient.objects.create(
            name=name, type=IngredientType.FRUIT, **{**defaults, **extras}
        )

class VegetableFactory(IngredientFactory):
    def create(self, name, **extras):
        defaults = dict(calories=40, fats=0.1, carbs=8)
        return Ingredient.objects.create(
            name=name, type=IngredientType.VEGETABLE, **{**defaults, **extras}
        )
