from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")
    preview = models.ImageField(
        verbose_name="Превью курса",
        upload_to="education/course_preview/",
        null=True,
        blank=True,
    )
    description = models.TextField(verbose_name="Описание курса")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(verbose_name="Название урока", max_length=300)
    description = models.TextField(verbose_name="Описание урока")
    preview = models.ImageField(
        verbose_name="Превью урока",
        upload_to="education/lesson_preview/",
        null=True,
        blank=True,
    )
    url_video = models.CharField(
        verbose_name="Ссылка на видео", max_length=300, null=True, blank=True
    )

    course = models.ForeignKey(Course, verbose_name="курс", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
