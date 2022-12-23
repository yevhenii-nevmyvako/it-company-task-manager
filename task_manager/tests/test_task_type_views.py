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

    def test_delete_task_type_login_required(self):
        """test doesn't open task_type_delete_confirm without login"""
        task_type = TaskType.objects.create(
            name="test"
        )
        url_to_delete = reverse(
            "task_manager:task-type-delete", args=[task_type.id]
        )
        response = self.client.get(url_to_delete)

        self.assertNotEqual(response.status_code, 200)

    def test_detail_task_type_login_required(self):
        """test doesn't open task_type_detail without login"""
        task_type = TaskType.objects.create(
            name="test"
        )
        url_to_detail = reverse(
            "task_manager:task-type-detail", args=[task_type.id]
        )
        response = self.client.get(url_to_detail)

        self.assertNotEqual(response.status_code, 200)

    def test_update_task_type_login_required(self):
        """test doesn't open task_type_form without login"""
        task_type = TaskType.objects.create(
            name="test"
        )
        url_to_update = reverse(
            "task_manager:task-type-update", args=[task_type.id]
        )
        response = self.client.get(url_to_update)

        self.assertNotEqual(response.status_code, 200)


class PrivateTaskTypeTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="qwer1234"
        )
        self.client.force_login(self.user)



