from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Instructions(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название иструкции', blank=False, null=False)
    object = models.CharField(max_length=60, verbose_name='Предметная область', blank=False, null=False)
    instuctions = models.CharField(max_length=10, verbose_name='Заглушка не забудь', blank=True, null=True)
    reed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Инструкции"
        verbose_name_plural = "Инструкция"

class Posts(models.Model):
    title = models.CharField(max_length=60, verbose_name='Должность', blank=False, null=False)
    instuctions = models.ForeignKey(Instructions, on_delete=models.PROTECT, related_name='instuction')
    allowance = models.CharField(max_length=30, verbose_name='Допуск', blank=True, null=True)
    allowance_level = models.PositiveSmallIntegerField(verbose_name='Уровень доступа', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Должности"
        verbose_name_plural = "Должность"

class Office(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название подразделения', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подразделения"
        verbose_name_plural = "Подразделение"

class Person(AbstractUser):
    foto = models.CharField(max_length=10, blank=True, null=True)
    post = models.ForeignKey(Posts, on_delete=models.PROTECT, related_name='post', null=True, blank=True,)
    allowance = models.ForeignKey(Posts, on_delete=models.PROTECT, null=True, blank=True, related_name='allowances')
    office = models.ForeignKey(Office, on_delete=models.PROTECT, related_name='offices', null=True, blank=True)

    def __str__(self):
        return f'{self.username} {self.first_name} {self.last_name}'

    class Meta(AbstractUser.Meta):
        verbose_name = "Сотрудники"
        verbose_name_plural = "Сотрудник"

