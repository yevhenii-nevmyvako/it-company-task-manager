from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import TaskType, Task, Position, Worker


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["is_completed", "priority", "task_type", "deadline", "description"]
    list_filter = ["is_completed", "priority", "deadline"]
    search_fields = ["task_type"]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


admin.site.register(Worker, UserAdmin)
