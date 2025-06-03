from django.urls import path
from . import views

urlpatterns = [
    path(
        "monthly-served/",
        views.MonthlyServedChartView.as_view(),
        name="monthly-served",
    ),
    path(
        "monthly-served/data/",
        views.MonthlyServedData.as_view(),
        name="monthly-served-data",
    ),
]
