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
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="task")
    created = models.DateTimeField("Дата добавления", auto_now_add=True,
                                   db_index=True)
    status = models.CharField(max_length=10, choices=STATUSES, default='new')
    finished = models.DateField("Дата завершения")

    def __str__(self):
        return self.title


