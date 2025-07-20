from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'study-items', views.StudyItemViewSet)

urlpatterns = router.urls


