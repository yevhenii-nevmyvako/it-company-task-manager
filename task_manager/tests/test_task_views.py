from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Project, Team

TASK_URL = reverse("task_manager:task-list")
TASK_CREATE_URL = reverse("task_manager:task-create")


class PublicTaskTests(TestCase):

    def test_task_open_list_required(self):
        """test login required in task
        list view doesn't work without login"""
        response = self.client.get(TASK_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_create_task_login_required(self):
        """test client doesn't open create
        task without login required"""
        response = self.client.get(TASK_CREATE_URL)

        self.assertNotEqual(response.status_code, 200)
