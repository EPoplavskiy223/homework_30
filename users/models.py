from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):

    username = None

    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="E-mail")

    phone = models.IntegerField(
        unique=True,
        verbose_name="Номер телефона",
        validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)],
        help_text="Введите номер телефона без кода страны",
    )

    city = models.CharField(verbose_name="Город", max_length=100)

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


# {
#     "first_name" : "Егор",
#     "last_name" : "Поплавский",
#     "email" : "test@gmail.com",
#     "phone" : "9774733818",
#     "city" : "Пушкино"
#     }
