from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    TASK_PRIORITY_CHOICES = (
        ("Ugent", "ugent priority task"),
        ("High", "high priority task"),
        ("Medium", "medium priority task"),
        ("Low", "low priority task"),
        ("Lowest", "lowest priority task"),
    )
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=TASK_PRIORITY_CHOICES)
    task_type = models.ForeignKey(
        TaskType, on_delete=models.CASCADE, related_name="tasks"
    )
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tasks")

    class Meta:
        ordering = ["-deadline"]

    def __str__(self):
        return (
            f"Task type: {self.task_type.name}"
            f" (deadline date: {self.deadline},"
            f" priority: {self.priority}"
        )


class Position(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workers",
        null=True
    )

    class Meta:
        ordering = ["username"]
        verbose_name = ["Worker"]
        verbose_name_plural = ["Workers"]

    def __str__(self):
        return (
            f"Username: {self.username} Full name: {self.first_name}"
            f" {self.last_name} Position: {self.position.name}"
        )
