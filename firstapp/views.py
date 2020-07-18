from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def show(request):
    response = datetime.datetime.now()
    return HttpResponse(response)