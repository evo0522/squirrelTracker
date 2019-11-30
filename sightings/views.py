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
	st_id = int(request.POST.get('st_id')[:-1])
	print("----------")
	print(request.POST.get('Running'))
	print("----------")



	print(st_id)
	sighting = Squirrel.objects.get(id=st_id)

	#get updated field
	n_Latitude = request.POST.get('Latitude')
	n_Longitude = request.POST.get('Longitude')
	n_Unique_Squirrel_ID = request.POST.get('Unique_Squirrel_ID')
	n_Date = request.POST.get('Date') # TODO
	n_Age = request.POST.get('Age')
	n_Shift = request.POST.get('Shift')
	n_Primary_Fur_Color = request.POST.get('Primary_Fur_Color')
	n_Location = request.POST.get('Location')
	n_Specific_Location = request.POST.get('Specific_Location')
	n_Other_Activities = request.POST.get('Other_Activities')
	# print(request.POST.get('Running'))
	#Boolean
	n_Running = True if "true" in request.POST.get('Running').lower() else False
	n_Chasing = True if "true" in request.POST.get('Chasing').lower() else False
	n_Climbing = True if "true" in request.POST.get('Climbing').lower() else False
	n_Eating = True if "true" in request.POST.get('Eating').lower() else False
	n_Foraging = True if "true" in request.POST.get('Foraging').lower() else False
	
	n_Kuks = True if "true" in request.POST.get('Kuks').lower() else False
	n_Quaas = True if "true" in request.POST.get('Quaas').lower() else False
	n_Moans = True if "true" in request.POST.get('Moans').lower() else False
	n_Tail_flags = True if "true" in request.POST.get('Tail_flags').lower() else False
	n_Tail_twitches = True if "true" in request.POST.get('Tail_twitches').lower() else False
	
	n_Approaches = True if "true" in request.POST.get('Approaches').lower() else False
	n_Indifferent = True if "true" in request.POST.get('Indifferent').lower() else False
	n_Runs_from = True if "true" in request.POST.get('Runs_from').lower() else False

	#update 
	sighting.Latitude = n_Latitude
	sighting.Longitude = n_Longitude
	sighting.Unique_Squirrel_ID = n_Unique_Squirrel_ID
	sighting.Date = n_Date
	sighting.Age = n_Age
	
	sighting.Shift = n_Shift
	sighting.Shift = n_Shift
	sighting.Primary_Fur_Color = n_Primary_Fur_Color
	sighting.Location = n_Location
	sighting.Specific_Location = n_Specific_Location
	
	sighting.Other_Activities = n_Other_Activities
	#Boolean
	sighting.Running = n_Running
	sighting.Chasing = n_Chasing
	sighting.Climbing = n_Climbing
	sighting.Eating = n_Eating
	sighting.Foraging = n_Foraging

	sighting.Kuks = n_Kuks
	sighting.Quaas = n_Quaas
	sighting.Moans = n_Moans
	sighting.Tail_flags = n_Tail_flags
	sighting.Tail_twitches = n_Tail_twitches

	sighting.Approaches = n_Approaches
	sighting.Indifferent = n_Indifferent
	sighting.Runs_from = n_Runs_from

	#save
	sighting.save()
	squirrels = Squirrel.objects.all()
	context = {
		'squirrels':squirrels
	}
	return render(request,'sightings/all.html',context)