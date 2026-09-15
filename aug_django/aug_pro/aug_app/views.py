from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def demo(request):
    return HttpResponse("hi,this is neebha its my my first django project...")