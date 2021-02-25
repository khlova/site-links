from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default='admin')
    long_link = models.CharField(verbose_name='Длинная ссылка', max_length=200)
    short_link = models.CharField(verbose_name='Сокращенная ссылка', max_length=30, unique=False)


    def __str__(self):
        # return f'Пользователь с id: {self.user.id}, ссылка: {self.short_link}'
        return self.short_link

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
