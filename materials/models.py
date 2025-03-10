from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название курса")
    preview = models.ImageField(verbose_name="Фотография", blank=True, null=True)
    description = models.TextField(verbose_name="Описание курса", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название урока")
    description = models.TextField(
        max_length=200, verbose_name="Описание курса", blank=True, null=True
    )
    preview = models.ImageField(verbose_name="Фотография", blank=True, null=True)
    video_link = models.TextField(
        max_length=200, verbose_name="Ссылка на видео", blank=True, null=True
    )

    course = models.ForeignKey(Course, related_name="lessons", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
