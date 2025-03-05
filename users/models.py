from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=50, unique=False, blank=True, null=True, default=""
    )
    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(
        max_length=35,
        verbose_name="Phone",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
        blank=True,
        null=True,
        help_text="Введите страну",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Avatar",
        blank=True,
        null=True,
        help_text="Загрузите свой аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
