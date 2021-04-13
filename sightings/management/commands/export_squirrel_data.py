from django.core.management import BaseCommand
import csv
from map.models import Squirrel
import sys


class Command(BaseCommand):
    help = 'Export Squirrel dataset'

    def add_arguments(self, parser):
        parser.add_argument('path',type=str,help="csv file")

    def handle(self, path, **options):
        with open(path, 'w', newline='') as c:
            model = Squirrel
            field_names = [f.name for f in model._meta.fields]
            writer = csv.writer(c, quoting=csv.QUOTE_ALL)
            writer.writerow(field_names)
            for each in model.objects.all():
                writer.writerow([getattr(each, f) for f in field_names])

