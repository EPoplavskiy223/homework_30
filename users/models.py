import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from education.models import Course, Lesson


class User(AbstractUser):

    username = None

    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="E-mail")

    phone = models.CharField(
        unique=True,
        verbose_name="Номер телефона",
        max_length=20,
        null=True,
        blank=True,
    )

    city = models.CharField(verbose_name="Город", max_length=100, null=True, blank=True)

    avatar = models.ImageField(
        verbose_name="Аватарка", upload_to="users/avatar/", null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):

    STATUS_CASH = "cash"
    STATUS_TRANSFER_TO_ACCOUNT = "transfer to account"
    STATUS_FAILED = "Не оплачено"
    STATUS_CHOICES = [
        (STATUS_CASH, "Наличными"),
        (STATUS_TRANSFER_TO_ACCOUNT, "Перевод на счет"),
        (STATUS_FAILED, "Не оплачено"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField(
        default=datetime.date.today, verbose_name="Дата оплаты"
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Оплаченный курс",
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Оплаченный урок",
    )
    payment_amount = models.IntegerField(default=0, verbose_name="Сумма оплаты")
    payment_method = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_FAILED,
        verbose_name="Способ оплаты",
    )

    def save(self, *args, **kwargs):
        if self.payment_amount == 0:
            self.payment_method = self.STATUS_FAILED
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
