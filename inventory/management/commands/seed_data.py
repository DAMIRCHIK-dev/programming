# inventory/management/commands/seed_data.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
import random
from datetime import datetime, timedelta

from inventory.models import Ingredient, IngredientDelivery
from meals.models import Meal, MealIngredient, ServedMeal

class Command(BaseCommand):
    help = "Seed database with sample data using Faker"

    def handle(self, *args, **kwargs):
        fake = Faker()
        User = get_user_model()

        # 1. Create 5 users
        users = []
        for _ in range(5):
            username = fake.user_name()
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'email': fake.email()}
            )
            if created:
                user.set_password('password123')
                user.save()
            users.append(user)
        self.stdout.write(self.style.SUCCESS("✔ Created 5 users"))

        # 2. Create 10 ingredients
        ingredients = []
        for _ in range(10):
            ing = Ingredient.objects.create(
                name=fake.unique.word().capitalize(),
                quantity=random.uniform(500, 3000),
                min_quantity=random.uniform(50, 300)
            )
            ingredients.append(ing)
        self.stdout.write(self.style.SUCCESS("✔ Created 10 ingredients"))

        # 3. Create 20 deliveries over past 3 months
        for _ in range(20):
            date = datetime.now() - timedelta(days=random.randint(1, 90))
            IngredientDelivery.objects.create(
                ingredient=random.choice(ingredients),
                quantity=random.uniform(50, 500),
                delivery_date=date,
                created_by=random.choice(users)
            )
        self.stdout.write(self.style.SUCCESS("✔ Created 20 deliveries"))

        # 4. Create 5 meals
        meals = []
        for _ in range(5):
            meal = Meal.objects.create(
                name=fake.unique.sentence(nb_words=2).rstrip('.'),
                description=fake.text(max_nb_chars=200)
            )
            meals.append(meal)
        self.stdout.write(self.style.SUCCESS("✔ Created 5 meals"))

        # 5. Assign 2–5 random ingredients to each meal
        for meal in meals:
            for ing in random.sample(ingredients, k=random.randint(2,5)):
                MealIngredient.objects.create(
                    meal=meal,
                    ingredient=ing,
                    quantity_required=random.uniform(20, 200)
                )
        self.stdout.write(self.style.SUCCESS("✔ Assigned ingredients to meals"))

        # 6. Create ServedMeal entries for last 6 months
        now = datetime.now()
        for month_offset in range(6, -1, -1):
            base = now - timedelta(days=30 * month_offset)
            for _ in range(random.randint(3, 6)):
                served_date = base + timedelta(
                    days=random.randint(0,29),
                    hours=random.randint(0,23),
                    minutes=random.randint(0,59)
                )
                ServedMeal.objects.create(
                    meal=random.choice(meals),
                    served_by=random.choice(users),
                    served_at=served_date,
                    success=random.choice([True, True, False])
                )
        self.stdout.write(self.style.SUCCESS("✔ Created served meal records"))
