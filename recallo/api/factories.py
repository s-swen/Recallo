import factory
from factory.django import DjangoModelFactory

from .models import StudyItem

class StudyItemFactory(DjangoModelFactory):
    class Meta:
        model = StudyItem
    