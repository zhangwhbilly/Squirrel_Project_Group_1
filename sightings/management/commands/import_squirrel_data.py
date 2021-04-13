from django.core.management import BaseCommand
import csv
import datetime
from distutils.util import strtobool
from map.models import Squirrel

class Command(BaseCommand):
    help='Import Squirrel Dataset'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type= str)

    def handle(self, *args, **options):
        with open(options['csv_file']) as c:
            reader = csv.DictReader(c)
            import_data = list(reader)
        for each in import_data:
            df = Squirrel(
                longitude = each['X'],
                latitude = each['Y'],
                shift = each['Shift'],
                date=datetime.datetime.strptime(each['Date'].strip(), '%m%d%Y').date(),
                unique_squirrel_id = each['Unique Squirrel ID'],
                age = each['Age'],
                primary_fur_color = each['Primary Fur Color'],
                location = each['Location'],
                specific_location = each['Specific Location'],
                running = strtobool(each['Running']),
                chasing = strtobool(each['Chasing']),
                climbing = strtobool(each['Climbing']),
                eating = strtobool(each['Eating']),
                foraging = strtobool(each['Foraging']),
                other_activities = each['Other Activities'],
                kuks = strtobool(each['Kuks']),
                quaas = strtobool(each['Quaas']),
                moans = strtobool(each['Moans']),
                tail_flags = strtobool(each['Tail flags']),
                tail_twitching = strtobool(each['Tail twitches']),
                approaches = strtobool(each['Approaches']),
                indifferent = strtobool(each['Indifferent']),
                runs_from = strtobool(each['Runs from']),
            )

            df.save()
        
