import csv

from django.core.management.base import BaseCommand

from actors.models import Actor

from datetime import datetime


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path', type=str, help='The file path of the CSV file to import.'
        )

    def handle(self, *args, **options):
        file = options['file_path']

        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['name'],
                birth_date = datetime.strptime(row['birth_date'], '%d-%m-%Y').date(),
                nationality = row['nationality']

            Actor.objects.create(
                name=name,
                birth_date=birth_date,
                nationality=nationality)
