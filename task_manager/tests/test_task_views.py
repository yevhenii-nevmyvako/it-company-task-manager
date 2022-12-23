from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Project, Team, Task, TaskType

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

    def test_delete_task_login_required(self):
        """test doesn't open task_delete_confirm without login"""
        task_type = TaskType.objects.create(name="test1")
        task = Task.objects.create(
            task_type=task_type
        )
        url_to_delete = reverse(
            "task_manager:task-delete", args=[task.id]
        )
        response = self.client.get(url_to_delete)

        self.assertNotEqual(response.status_code, 200)

    def test_detail_task_login_required(self):
        """test doesn't open task_detail without login"""
        task_type = TaskType.objects.create(name="test1")
        task = Task.objects.create(
            task_type=task_type
        )
        url_to_detail = reverse(
            "task_manager:team-detail", args=[task.id]
        )
        response = self.client.get(url_to_detail)

        self.assertNotEqual(response.status_code, 200)

    def test_update_team_login_required(self):
        """test doesn't open team_form without login"""
        task_type = TaskType.objects.create(name="test1")
        task = Task.objects.create(
            task_type=task_type
        )
        url_to_update = reverse(
            "task_manager:team-update", args=[task.id]
        )
        response = self.client.get(url_to_update)

        self.assertNotEqual(response.status_code, 200)
