import pytest
from django.core import management
from django.core.management.commands import loaddata

'''
@pytest.fixture
def create_admin_user(django_user_model):
    """
        Retorna o usuario administrador
    """
    return django_user_model.objects.create_superuser("admin", "a@a.com", "password")
'''

@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
        Carregando dados da fixture no DB
    """

    with django_db_blocker.unblock():
        management.call_command("loaddata", "db_admin_fixture.json")
        management.call_command("loaddata", "db_category_fixture.json")

