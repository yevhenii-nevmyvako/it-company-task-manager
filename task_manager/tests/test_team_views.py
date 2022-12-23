from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Project, Team

TEAM_URL = reverse("task_manager:team-list")
TEAM_CREATE_URL = reverse("task_manager:team-create")


