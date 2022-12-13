from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("task_manager:task-type-detail", args=[str(self.id)])


class Team(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        constraints = [
            UniqueConstraint(
                name="unique_team_name", fields=["name"]
            )
        ]

    def get_absolute_url(self):
        return reverse("task_manager:team-detail", args=[str(self.id)])


class Project(models.Model):
    name = models.CharField(max_length=255)
    teams = models.ManyToManyField(
        Team, related_name="projects",
        required=False
    )
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["name"]
        constraints = [
            UniqueConstraint(
                name="unique_project_name", fields=["name"]
            )
        ]

    def __str__(self):
        return f"Project: {self.name}" \
               f"Teams:{self.teams.name}"

    def get_absolute_url(self):
        return reverse("task_manager:project-detail", args=[str(self.id)])


class Task(models.Model):
    TASK_PRIORITY_CHOICES = (
        ("ugent", "Ugent priority task"),
        ("high", "High priority task"),
        ("medium", "Medium priority task"),
        ("low", "Low priority task"),
        ("lowest", "Lowest priority task"),
    )
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=TASK_PRIORITY_CHOICES)
    task_type = models.ForeignKey(
        TaskType, on_delete=models.CASCADE, related_name="tasks"
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
        required=False,
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name="tasks",
        required=False,
    )

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return (
            f"Task type: {self.task_type.name}"
            f" (deadline date: {self.deadline},"
            f" priority: {self.priority}"
        )

    def get_absolute_url(self):
        return reverse("task_manager:task-detail", args=[str(self.id)])


class Position(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["name"]
        constraints = [
            UniqueConstraint(
                name="unique_position_name", fields=["name"]
            )
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("task_manager:position-detail", args=[str(self.id)])


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="workers",
        null=True,
        required=False,
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="workers",
        null=True,
        required=False,
    )

    class Meta:
        ordering = ["username"]
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        return (
            f"Username: {self.username} Full name: {self.first_name}"
            f" {self.last_name} Position: "
        )

    def get_absolute_url(self):
        return reverse("task_manager:worker-detail", args=[str(self.id)])
