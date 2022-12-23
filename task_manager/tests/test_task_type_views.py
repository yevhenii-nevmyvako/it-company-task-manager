from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import TaskType


POSITION_URL = reverse("task_manager:task-type-list")
POSITION_CREATE_URL = reverse("task_manager:task-type-create")


class PublicTaskTypeTests(TestCase):

    def test_task_type_open_list_required(self):
        """test login required in task type
        list view doesn't work without login"""
        response = self.client.get(POSITION_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_create_task_type_login_required(self):
        """test client doesn't open create
        task type without login required"""
        response = self.client.get(POSITION_CREATE_URL)

        self.assertNotEqual(response.status_code, 200)

