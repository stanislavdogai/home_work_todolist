from django.db import models


status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=1000, blank=False, null=False, verbose_name='Описание')
    status = models.CharField(max_length=100, choices=status_choices, default='new', blank=False, null=False, verbose_name='Статус')
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.pk}. {self.description}'

    class Meta:
        db_table = 'task'
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'