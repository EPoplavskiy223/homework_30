from rest_framework.serializers import ModelSerializer, SerializerMethodField

from education.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "course"]


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "description"]


class CourseDetailSerializer(ModelSerializer):

    lesson = SerializerMethodField()
    count_lesson_with_same_course = SerializerMethodField()

    def get_lesson(self, course):
        """Вывод названия урока в курсе"""
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    @staticmethod
    def get_count_lesson_with_same_course(course):
        """Количество уроков в курсе"""
        return course.lesson_set.count()

    class Meta:
        model = Course
        fields = ["name", "description", "lesson", "count_lesson_with_same_course"]