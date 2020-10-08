from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    STATUSES = [
        ('new', 'new'),
        ('planned', 'planned'),
        ('in work', 'in work'),
        ('finished', 'finished'),
    ]
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="tasks")
    created = models.DateTimeField("Дата добавления", auto_now_add=True,
                                   db_index=True)
    status = models.CharField(max_length=10, choices=STATUSES, default='new')
    finished = models.DateField("Дата завершения", null=True, blank=True,
                                default=None)

    def __str__(self):
        return self.title


class History(models.Model):
    STATUSES = [
        ('new', 'new'),
        ('planned', 'planned'),
        ('in work', 'in work'),
        ('finished', 'finished'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments")
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             related_name="history")
    status = models.CharField(max_length=10, choices=STATUSES)
    created = models.DateTimeField("Дата создания статуса", auto_now_add=True,
                                   db_index=True)
