from django.http import HttpResponse
from django.shortcuts import render

from .models import Squirrel
import datetime as dt

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#all squirel list 
def list(request):
	squirrels = Squirrel.objects.all()
	context = {
		'squirrels':squirrels
	}
	return render(request,'sightings/all.html',context)

