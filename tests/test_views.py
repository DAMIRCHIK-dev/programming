# tests/test_views.py
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from inventory.models import Ingredient

pytestmark = pytest.mark.django_db

def login_test_user(client):
    User = get_user_model()
    user = User.objects.create_user("tester", password="pass1234")
    client.login(username="tester", password="pass1234")
    return user

def test_inventory_list_status(client):
    url = reverse("ingredient-list-root")      # path("")  in inventory.urls
    resp = client.get(url)
    assert resp.status_code == 200

def test_delivery_create_requires_login(client):
    url = reverse("delivery-create")           # /deliveries/new/
    resp = client.get(url)
    assert resp.status_code == 302 and "/login" in resp.headers["Location"]

def test_delivery_create_logged_in(client):
    login_test_user(client)
    Ingredient.objects.create(name="Sugar", quantity=500, min_quantity=50)
    url = reverse("delivery-create")
    resp = client.get(url)
    assert resp.status_code == 200
