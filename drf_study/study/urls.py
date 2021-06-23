from django.urls import path

from .api import StudyList, StudyDetail

urlpatterns = [
    path("api/study/", StudyList.as_view(), name="api/study"),
    path("api/study/<int:pk>/", StudyDetail.as_view(),
         name="api/study")
]
