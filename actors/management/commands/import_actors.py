from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path', type=str, help='The file path of the CSV file to import.'
        )

    def handle(self, *args, **options):
        file = options['file_path']

        print(
            f"fImporting actors to the database... file: {file}"
        )
