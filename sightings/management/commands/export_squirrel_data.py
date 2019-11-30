# Todo export
from django.core.management.base import BaseCommand 
from sightings.models import Squirrel
from django.http import HttpResponse
import csv 
import sys


class Command(BaseCommand):
	help = 'Export data to csv'

	def add_arguements(self, parser):
		parser.add_argument('path')

	def handle(self,*args, **operant):
		 meta = Squirrel._meta
		 field_names = [field.name for field in meta.fields]
		 file_path = operant['path']

		 with open(file_path, 'w') as outputfile:
		 	writer = csv.writer(outputfile)
		 	writer.writerow(field_names)
		 	for item in Squirrel.objects.all():
		 		writer.writerow([getattr(item, field) for field in field_names])

