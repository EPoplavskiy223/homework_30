from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from education.models import Course, Lesson
from education.serializers import (CourseDetailSerializer, CourseSerializer,
                                   LessonSerializer)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class CourseListApiView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveApiView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class CourseCreateApiView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateApiView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDestroyApiView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
