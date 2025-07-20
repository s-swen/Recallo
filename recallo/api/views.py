from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import StudyItem
from .serializers import StudyItemSerializer

# Create your views here.
class StudyItemViewSet(ModelViewSet):
    queryset = StudyItem.objects.all()
    serializer_class = StudyItemSerializer
