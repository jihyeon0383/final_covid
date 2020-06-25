# chart/views.py
from django.shortcuts import render
from .models import Covid
from django.db.models import Sum


def home(request):
    return render(request, 'home.html')


def covid(request):
    dataset = Covid.objects \
        .values('country') \
        .annotate(
        confirmed=Sum('country', 'date'),
        recovered = Sum('country', 'date'),
        deaths = Sum('country', 'date'))\
        .order_by('country')
    return render(request, 'covid.html', {'dataset': dataset})

def recovered(request):
    dataset = Covid.objects \
        .values('country') \
        .annotate(
        confirmed=Sum('country', 'date'),
        recovered = Sum('country', 'date'),
        deaths = Sum('country', 'date'))\
        .order_by('country')
    return render(request, 'recovered.html', {'dataset': dataset})

def deaths(request):
    dataset = Covid.objects \
        .values('country') \
        .annotate(
        confirmed=Sum('country', 'date'),
        recovered = Sum('country', 'date'),
        deaths = Sum('country', 'date'))\
        .order_by('country')
    return render(request, 'deaths.html', {'dataset': dataset})


