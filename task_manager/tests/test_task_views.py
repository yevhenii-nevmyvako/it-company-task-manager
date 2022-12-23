from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Project, Team

PROJECT_URL = reverse("task_manager:task-list")
PROJECT_CREATE_URL = reverse("task_manager:task-create")
