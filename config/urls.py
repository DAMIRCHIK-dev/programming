# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # ――― “/” dan to‘g‘ridan-to‘g‘ri Inventory sahifasiga yo‘naltirish ―――
    path("", RedirectView.as_view(pattern_name="ingredient-list-root", permanent=False)),

    # Admin panel
    path("admin/", admin.site.urls),

    # App URL’lari
    path("api/inventory/", include("inventory.urls")),
    path("api/meals/",     include("meals.urls")),
    path("api/users/",     include("users.urls")),
    path("reports/",       include("reports.urls")),
]
