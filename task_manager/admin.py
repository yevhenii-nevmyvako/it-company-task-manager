from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import (
    TaskType,
    Task,
    Position,
    Worker,
    Project,
    Team,
)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "is_completed",
        "priority",
        "task_type",
        "deadline",
        "description",
    ]
    list_filter = ["is_completed", "priority", "deadline"]
    search_fields = ["task_type"]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info: position", {"fields": ("position",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": (
            "first_name", "last_name", "email", "position", "team"
        )}),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "team"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]
