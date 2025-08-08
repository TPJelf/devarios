from django.urls import path
from . import views

urlpatterns = [
    path("", views.incident_list, name="landing"),
    path("incidents/", views.incident_list, name="incident_list"),
    path("sources/", views.source_list, name="source_list"),
]
