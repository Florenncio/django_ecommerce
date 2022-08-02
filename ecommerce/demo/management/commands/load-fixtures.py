from django.core import management
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwards):
        management.call_command("makemigrations")
        management.call_command("migrate")
        management.call_command("loaddata", "db_admin_fixture.json")
        management.call_command("loaddata", "db_category_fixture.json")