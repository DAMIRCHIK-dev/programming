from rest_framework import serializers
from .models import Ingredient, IngredientDelivery

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class IngredientDeliverySerializer(serializers.ModelSerializer):
    ingredient_name = serializers.CharField(source="ingredient.name", read_only=True)

    class Meta:
        model = IngredientDelivery
        fields = "__all__"
