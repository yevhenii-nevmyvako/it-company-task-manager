from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import TaskType


TASK_TYPE_URL = reverse("task_manager:task-type-list")
TASK_TYPE_CREATE_URL = reverse("task_manager:task-type-create")


class PublicTaskTypeTests(TestCase):

    def test_task_type_open_list_required(self):
        """test login required in task type
        list view doesn't work without login"""
        response = self.client.get(TASK_TYPE_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_create_task_type_login_required(self):
        """test client doesn't open create
        task type without login required"""
        response = self.client.get(TASK_TYPE_CREATE_URL)

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

    def test_task_type_open_with_login_required(self):
        """test to open task type list with login required"""
        response = self.client.get(TASK_TYPE_URL)

        self.assertEqual(response.status_code, 200)

    def test_create_task_type_open_with_login_required(self):
        """test client open create task type with login required"""
        response = self.client.get(TASK_TYPE_CREATE_URL)

        self.assertEqual(response.status_code, 200)

    def test_create_task_type_with_login_required(self):
        """test should create task type with user login"""
        TaskType.objects.create(name="test")
        response = self.client.get(TASK_TYPE_CREATE_URL)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_task_type_detail_with_login(self):
        """test retrieved task type detail page with login required"""
        task_type = TaskType.objects.create(
            name="test"
        )
        url_to_detail = reverse(
            "task_manager:task-type-detail", args=[task_type.id]
        )
        response = self.client.get(url_to_detail)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_task_type_delete_with_login(self):
        """test retrieved position delete page with login required"""
        task_type = TaskType.objects.create(
            name="test"
        )
        url_to_delete = reverse(
            "task_manager:task-type-delete", args=[task_type.id]
        )
        response = self.client.get(url_to_delete)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_task_type_update_with_login(self):
        """test retrieved task type delete page with login required"""
        task_type = TaskType.objects.create(
            name="test"
        )
        url_to_update = reverse(
            "task_manager:task-type-update", args=[task_type.id]
        )
        response = self.client.get(url_to_update)

        self.assertEqual(response.status_code, 200)




