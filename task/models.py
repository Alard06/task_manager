from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE,
                                )


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    

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
    description = models.TextField(verbose_name='Описание',
                                   blank=True)
    owner = models.ForeignKey(Profile, 
                              on_delete=models.CASCADE,
                              related_name='owner',
                              verbose_name='Владелец')
    status = models.ForeignKey(Status, 
                               on_delete=models.CASCADE,
                               verbose_name='Статус')
    executor = models.ManyToManyField(Profile, 
                              through='UserTasks',
                              verbose_name='Исполнитель',
                              blank=True
                              )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    check = models.BooleanField(default=False,
                                verbose_name='Выполнено')
    published = models.BooleanField(default=False,
                                verbose_name='Публикация')


    class Meta:
        verbose_name = 'задачу'
        verbose_name_plural = 'Задачи'
        ordering = ['id',]

    def __str__(self):
        return self.title 

class UserTasks(models.Model):

    user = models.ForeignKey(Profile, 
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    tasks = models.ForeignKey(Task, 
                              on_delete=models.CASCADE,
                              verbose_name='Задачи')



