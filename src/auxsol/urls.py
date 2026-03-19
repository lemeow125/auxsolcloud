from django.urls import path
from . import views

urlpatterns = [
    path("analytics/latest/", views.get_analytics, name="latest-analytics"),
    path("analytics/report/latest/",
         views.get_inverter_report, name="latest-inverter-report"),
    path("inverter/latest/", views.get_inverter, name="latest-data")
]
