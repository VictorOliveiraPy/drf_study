from django.urls import path

from .api import StudyList

urlpatterns = [
    path("api/study/", StudyList.as_view(), name="api/study"),
]
