from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request,chinna):
    return HttpResponse(f'Happy new year {chinna}')