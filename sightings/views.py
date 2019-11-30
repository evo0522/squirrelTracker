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

def add(request):
	return render(request,'sightings/add.html')

def add_sighting_from_submission(request):
	print("add form is submitted")
	
	Latitude = request.POST.get('Latitude')
	Longitude = request.POST.get('Longitude')
	Unique_Squirrel_ID = request.POST.get('Unique_Squirrel_ID')
	Date = request.POST.get('Date') # TODO
	Age = request.POST.get('Age')
	Shift = request.POST.get('Shift')
	Primary_Fur_Color = request.POST.get('Primary_Fur_Color')
	Location = request.POST.get('Location')
	Specific_Location = request.POST.get('Specific_Location')
	Other_Activities = request.POST.get('Other_Activities')
	# print(request.POST.get('Running'))

	#Boolean
	Running = True if "true" in request.POST.get('Running').lower() else False
	Chasing = True if "true" in request.POST.get('Chasing').lower() else False
	Climbing = True if "true" in request.POST.get('Climbing').lower() else False
	Eating = True if "true" in request.POST.get('Eating').lower() else False
	Foraging = True if "true" in request.POST.get('Foraging').lower() else False
	Kuks = True if "true" in request.POST.get('Kuks').lower() else False
	Quaas = True if "true" in request.POST.get('Quaas').lower() else False
	Moans = True if "true" in request.POST.get('Moans').lower() else False
	Tail_flags = True if "true" in request.POST.get('Tail_flags').lower() else False
	Tail_twitches = True if "true" in request.POST.get('Tail_twitches').lower() else False
	Approaches = True if "true" in request.POST.get('Approaches').lower() else False
	Indifferent = True if "true" in request.POST.get('Indifferent').lower() else False
	Runs_from = True if "true" in request.POST.get('Runs_from').lower() else False
	# print(Latitude,Longitude,Age,Shift,Primary_Fur_Color,Location,Specific_Location,Other_Activities)
	# print(Running,Chasing,Runs_from)
	squirrel,created = Squirrel.objects.get_or_create(
                         Longitude = Longitude,
                         Latitude = Latitude,
                         Unique_Squirrel_ID = Unique_Squirrel_ID,
                         Date = dt.datetime.strptime(Date.strip(),'%m%d%Y').date(),
                         Age = Age,
                         Shift = Shift,
                         Primary_Fur_Color = Primary_Fur_Color,
                         Location = Location,
                         Specific_Location = Specific_Location,
                         Other_Activities = Other_Activities,
                         Running = Running,
                         Chasing = Chasing,
                         Climbing = Climbing,
                         Eating = Eating,
                         Foraging = Foraging,
                         Kuks = Kuks,
                         Quaas = Quaas,
                         Moans = Moans,
                         Tail_flags = Tail_flags,
                         Tail_twitches = Tail_twitches,
                         Approaches = Approaches,
                         Indifferent = Indifferent,
                         Runs_from = Runs_from,
                         )
	if created:
		squirrel.save()
	print("new sighting addd")
	squirrels = Squirrel.objects.all()
	context = {
		'squirrels':squirrels
	}
	return render(request,'sightings/all.html',context)

def update_sighting_from_submission(request):
