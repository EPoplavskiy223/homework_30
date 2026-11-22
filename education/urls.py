from django.urls import path
from rest_framework.routers import SimpleRouter

from education.apps import EducationConfig
from education.views import (CourseCreateApiView, CourseDestroyApiView,
                             CourseListApiView, CourseRetrieveApiView,
                             CourseUpdateApiView, LessonViewSet)

app_name = EducationConfig.name

router = SimpleRouter()
router.register("", LessonViewSet)

urlpatterns = [
    path("course/", CourseListApiView.as_view(), name="course_list"),
    path("course/create/", CourseCreateApiView.as_view(), name="course_create"),
    path(
        "course/<int:pk>/delete/", CourseDestroyApiView.as_view(), name="course_delete"
    ),
    path(
        "course/<int:pk>/update/", CourseUpdateApiView.as_view(), name="course_update"
    ),
    path("course/<int:pk>/", CourseRetrieveApiView.as_view(), name="course_retrieve"),
]

urlpatterns += router.urls
