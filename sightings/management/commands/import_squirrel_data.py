# Todo 
# Importation 
import os 
import csv 
from django.core.management.base import BaseCommand 
from sightings.models import Squirrel
import datetime as dt


class Command(BaseCommand):
	"""docstring for Command"""
	help = 'import squirrel data csv'

	def add_arguments(self, parser):
		parser.add_argument('path')

	def handle(self,*args, **operant):
          path =  operant['path']
          #print(path)
          with open(path,'r') as file:
               data = csv.reader(file, delimiter=',')
               next(data,None)
               for row in data:
                    #print(row)
                    squirrel,created = Squirrel.objects.get_or_create(
                         Longitude = row[0],
                         Latitude = row[1],
                         Unique_Squirrel_ID = row[2],
                         Date = dt.datetime.strptime(row[5].strip(),'%m%d%Y').date(),
                         Age = row[7],
                         Shift = row[4],
                         Primary_Fur_Color = row[8],
                         Location = row[12],
                         Specific_Location = row[14],
                         Other_Activities = row[20],
                         Running = True if "true" in row[15].lower() else False,
                         Chasing = True if "true" in row[16].lower() else False,
                         Climbing = True if "true" in row[17].lower() else False,
                         Eating = True if "true" in row[18].lower() else False,
                         Foraging = True if "true" in row[19].lower() else False,
                         Kuks = True if "true" in row[21].lower() else False,
                         Quaas = True if "true" in row[22].lower() else False,
                         Moans = True if "true" in row[23].lower() else False,
                         Tail_flags = True if "true" in row[24].lower() else False,
                         Tail_twitches = True if "true" in row[25].lower() else False,
                         Approaches = True if "true" in row[26].lower() else False,
                         Indifferent = True if "true" in row[27].lower() else False,
                         Runs_from = True if "true" in row[28].lower() else False,
                         )
                    if created:
                         squirrel.save()