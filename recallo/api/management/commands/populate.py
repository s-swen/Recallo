from django.core.management.base import BaseCommand
from api.models import User
from api.factories import StudyItemFactory

class Command(BaseCommand):
    help = 'Creates users'
    def handle(self, *args, **kwargs):
        admin = User.objects.filter(username='admin').first()
        if not admin:
            admin = User.objects.create_superuser(
                username='admin', 
                email='admin@gmail.com', 
                password='admin'
                )
        user1 = User.objects.filter(username='user1').first()
        if not user1:
            user1 = User.objects.create_user(
                username='user1',
                email='user1@gmail.com',
                password='test'
            )
        user2 = User.objects.filter(username='user2').first()
        if not user2:
            user2 = User.objects.create_user(
                username='user2',
                email='user2@gmail.com',
                password='test'
            )
        for _ in range(10):
            StudyItemFactory(user=user1)
        for _ in range(10):
            StudyItemFactory(user=user2)
            