import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

from ecommerce.inventory import models

faker = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: "cat_slug_%d" % n)
    slug = faker.lexify(text='cat_slug_??????')

register(CategoryFactory)
        