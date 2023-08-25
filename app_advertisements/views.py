from django.http import HttpResponse
from django.shortcuts import render
from .models import Advertisement

def index(request):
    avertisements = Advertisement.objects.all()
    context = {'advertisements': avertisements}
    return render(request, 'index.html',context)

def lessonfour(request):
    return HttpResponse('урок номер 4')

def top_sellers(request):
    return render(request, 'top-sellers.html')