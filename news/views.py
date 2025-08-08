from django.shortcuts import render
from .models import Incident, Source


def incident_list(request):
    incidents = (
        Incident.objects.prefetch_related("article_set").all().order_by("-created_at")
    )
    return render(request, "news/incident_list.html", {"incidents": incidents})


def source_list(request):
    sources = Source.objects.all().order_by("name")
    return render(request, "news/source_list.html", {"sources": sources})
