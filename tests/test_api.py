# tests/test_api.py
import pytest
from rest_framework.test import APIClient
from inventory.models import Ingredient

pytestmark = pytest.mark.django_db

api = APIClient()

def test_api_inventory_json():
    Ingredient.objects.create(name="Salt", quantity=200, min_quantity=30)
    resp = api.get("/api/inventory/")           # ⬅️ URL moslashtirildi
    assert resp.status_code == 200
    assert resp.json()[0]["name"] == "Salt"

def test_api_meals_status():
    resp = api.get("/api/meals/meals/")
    assert resp.status_code == 200
