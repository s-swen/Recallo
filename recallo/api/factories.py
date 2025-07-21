import factory
from factory.django import DjangoModelFactory

from .models import StudyItem

class StudyItemFactory(DjangoModelFactory):
    class Meta:
        model = StudyItem
    
    user = factory.RequiredAttribute()
    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('paragraph', nb_sentences=4)