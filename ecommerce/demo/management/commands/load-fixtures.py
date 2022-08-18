from django.core import management
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwards):
        management.call_command("makemigrations")
        management.call_command("migrate")
        management.call_command("loaddata", "db_admin_fixture.json")
        management.call_command("loaddata", "db_category_fixture.json")
        management.call_command("loaddata", "db_product_fixture.json")
        management.call_command("loaddata", "db_category_product_fixture.json")
        management.call_command("loaddata", "db_brand_fixture.json")
        management.call_command("loaddata", "db_type_fixture.json")
        management.call_command("loaddata", "db_product_inventory_fixture.json")
        management.call_command("loaddata", "db_media_fixture.json")
        management.call_command("loaddata", "db_stock_fixture.json")
        management.call_command("loaddata", "db_product_attribute_fixture.json")
        management.call_command("loaddata", "db_product_attribute_value_fixture.json")
