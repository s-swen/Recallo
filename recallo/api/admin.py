from django.contrib import admin
from .models import StudyItem, User

@admin.register(StudyItem)
class StudyItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'created_at', 'updated_at']
    

