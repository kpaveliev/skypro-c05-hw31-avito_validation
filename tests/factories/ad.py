import factory

from ads.models import Ad
from .category import CategoryFactory
from .user import UserFactory


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test"
    price = 1000
    is_published = False
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
