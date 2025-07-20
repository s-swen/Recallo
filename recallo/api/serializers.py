from rest_framework import serializers
from .models import StudyItem

class StudyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyItem
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']