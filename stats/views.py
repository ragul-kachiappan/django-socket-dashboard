from django.shortcuts import render

from stats import models

# Create your views here.


def main(request):
    qs = models.Statistic.objects.all()
    return render(request, "stats/main.html", {"qs": qs})


def dashboard(request, slug):
    return render(request, "stats/dashboard.html", {})
