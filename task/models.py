from django.conf import settings
from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE,
                                primary_key = True)


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username
    

class Status(models.Model):
    # Статусы
    name = models.CharField(max_length=120, 
                            verbose_name='Статус')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    # Модель задач
    title = models.CharField(max_length=150, 
                             blank=True,
                             verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(Profile, 
                              on_delete=models.CASCADE,
                              related_name='owner')
    executor = models.ManyToManyField(Profile, 
                              through='UserTasks',
                              )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    check = models.BooleanField(default=False)
    status = models.ForeignKey(Status, 
                               on_delete=models.CASCADE)

class UserTasks(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)

