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

def single(request, st_id):
	if request.method == 'GET':
		squirrel = Squirrel.objects.get(id=st_id)
		context = {
			'squirrel':squirrel
		}
		print(squirrel.id)
		return render(request,'sightings/sighting.html',context)

	elif request.method == 'DELETE':
		st = Squirrel.objects.get(id=st_id)
		st_id = st.id
		st.delete()
		return HttpResponse('Sighting '+str(st_id)+' has been deleted')