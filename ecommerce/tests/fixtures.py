import pytest
from django.core import management
from django.core.management.commands import loaddata

@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
        Carregando dados da fixture no DB
    """

    with django_db_blocker.unblock():
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
