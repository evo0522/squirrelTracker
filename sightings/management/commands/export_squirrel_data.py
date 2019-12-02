from django.core.management import BaseCommand
from sightings.models import Squirrel
import csv
import sys

class Command(BaseCommand):
    help = 'export data'

    def add_arguments(self, parser):
        parser.add_argument('path',type=str,help="csv file")

    def handle(self, path, **options):
        with open(path, 'w', newline='') as f:
            model = Squirrel
            field_names = [fa.name for fa in model._meta.fields]
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(field_names)
            for instance in model.objects.all():
                writer.writerow([getattr(instance, fi) for fi in field_names])