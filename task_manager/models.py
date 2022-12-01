from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True)
    is_completed = models.BooleanField(default=False)


