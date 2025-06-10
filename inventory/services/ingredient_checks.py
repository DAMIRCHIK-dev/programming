
from abc import ABC, abstractmethod
from inventory.models import Inventory, IngredientQuantityError

class IngredientHandler(ABC):
    def __init__(self, nxt=None):
        self._next = nxt
    def set_next(self, nxt):
        self._next = nxt
        return nxt
    @abstractmethod
    def handle(self, meal):
        ...

class AvailabilityHandler(IngredientHandler):
    def handle(self, meal):
        for item in meal.items.all():
            if not item.ingredient.is_active:
                raise IngredientQuantityError(f"{item.ingredient.name} mavjud emas")
        return self._next.handle(meal) if self._next else True

class QuantityHandler(IngredientHandler):
    def handle(self, meal):
        for item in meal.items.all():
            left = Inventory.objects.get(ingredient=item.ingredient).quantity
            if left < item.quantity:
                raise IngredientQuantityError(f"{item.ingredient.name} yetarli emas")
        return self._next.handle(meal) if self._next else True
