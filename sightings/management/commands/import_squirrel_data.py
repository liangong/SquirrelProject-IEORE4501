from django.core.management.base import BaseCommand
from sightings.models import SquirrelData
from datetime import datetime
import csv


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str)

    def handle(self, *args, **kwargs):
        csv_path = kwargs['csv_path']
        try:
            with open(csv_path, encoding='utf-8') as f:
                f_csv = csv.DictReader(f)
                count = 0
                for row in f_csv:
                    try:
                        SquirrelData(
                            latitude=float(row['X']),
                            longitude=float(row['Y']),
                            unique_squirrel_id=row['Unique Squirrel ID'],
                            shift=row['Shift'],
                            date=datetime.strptime(row['Date'], '%m%d%Y'),
                            age=row['Age'],
                            primary_fur_color=row['Primary Fur Color'],
                            location=row['Location'],
                            specific_location=row['Specific Location'],
                            running=(True if row['Running'].lower() == 'true' else False),
                            chasing=(True if row['Chasing'].lower() == 'true' else False),
                            climbing=(True if row['Climbing'].lower() == 'true' else False),
                            eating=(True if row['Eating'].lower() == 'true' else False),
                            foraging=(True if row['Foraging'].lower() == 'true' else False),
                            other_activities=row['Other Activities'],
                            kuks=(True if row['Kuks'].lower() == 'true' else False),
                            quaas=(True if row['Quaas'].lower() == 'true' else False),
                            moans=(True if row['Moans'].lower() == 'true' else False),
                            tail_flags=(True if row['Tail flags'].lower() == 'true' else False),
                            tail_twitches=(True if row['Tail twitches'].lower() == 'true' else False),
                            approaches=(True if row['Approaches'].lower() == 'true' else False),
                            indifferent=(True if row['Indifferent'].lower() == 'true' else False),
                            runs_from=(True if row['Runs from'].lower() == 'true' else False),
                        ).save()
                        count += 1
                    except Exception as e:
                        print(e)
                        print('Import %s error' % row['Unique Squirrel ID'])
                print('Add %s sightings in total' % count)
        except Exception as e:
            print(e)
