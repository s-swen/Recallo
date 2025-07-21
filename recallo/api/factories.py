import factory
from factory.django import DjangoModelFactory

from .models import StudyItem

class StudyItemFactory(DjangoModelFactory):
    class Meta:
        model = StudyItem
    
    @factory.lazy_attribute
    def user(self):
        raise ValueError('You must provide a user')
    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('paragraph', nb_sentences=4)