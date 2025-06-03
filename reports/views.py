from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.functions import TruncMonth
from meals.models import ServedMeal


class MonthlyServedChartView(TemplateView):
    """
    HTML sahifa: Chart.js diagrammasi
    """
    template_name = "reports/monthly_served.html"


class MonthlyServedData(APIView):
    """
    /reports/monthly-served/data/  →  {"labels":[...],"data":[...]}
    """
    authentication_classes = []      # jamoatchi ko‘rishi mumkin — xohlasangiz token qo‘shing
    permission_classes = []

    def get(self, request):
        qs = (
            ServedMeal.objects.filter(success=True)
            .annotate(month=TruncMonth("served_at"))
            .values("month")
            .annotate(total=Count("id"))
            .order_by("month")
        )
        labels = [item["month"].strftime("%b %Y") for item in qs]
        data = [item["total"] for item in qs]
        return Response({"labels": labels, "data": data})
