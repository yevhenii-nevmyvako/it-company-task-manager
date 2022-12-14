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
        """test retrieved task type delete page with login required"""
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

    def test_equal_task_type_list_queryset_with_login(self):
        """test equal task type lists queryset with login required"""
        task_type_all = TaskType.objects.all()
        response = self.client.get(TASK_TYPE_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_type_list"]), list(task_type_all)
        )

    def test_retrieve_task_type_template_with_login(self):
        """test check task type template with login required"""
        response = self.client.get(TASK_TYPE_URL)

        self.assertTemplateUsed(
            response, "task_manager/task_type_list.html"
        )

    def test_retrieve_template_task_type_form_with_login(self):
        """test retrieve template task_type_form.html"""
        response = self.client.get(TASK_TYPE_CREATE_URL)

        self.assertTemplateUsed(
            response, "task_manager/task_type_form.html"
        )

    def test_retrieve_template_task_type_delete_confirm_with_login(self):
        """test retrieve template task_type_delete_confirm.html"""
        task_type = TaskType.objects.create(name="test")
        url_to_delete = reverse(
            "task_manager:task-type-delete", args=[task_type.id]
        )
        response = self.client.get(url_to_delete)

        self.assertTemplateUsed(
            response, "task_manager/task_type_delete_confirm.html"
        )

    def test_retrieve_template_task_type_detail_with_login(self):
        """test retrieve template task_type_detail.html"""
        task_type = TaskType.objects.create(name="test")
        url_to_detail = reverse(
            "task_manager:task-type-detail", args=[task_type.id]
        )
        response = self.client.get(url_to_detail)

        self.assertTemplateUsed(
            response, "task_manager/task_type_detail.html"
        )

    def test_retrieve_template_task_type_update_with_login(self):
        """test retrieve template task_type_form.html"""
        task_type = TaskType.objects.create(name="test")
        url_to_update = reverse(
            "task_manager:task-type-update", args=[task_type.id]
        )
        response = self.client.get(url_to_update)

        self.assertTemplateUsed(
            response, "task_manager/task_type_form.html"
        )

    def test_delete_required_in_detail_task_type_with_login(self):
        """test should delete the task_type"""
        task_type_delete = TaskType.objects.create(
            name="test")
        url_to_delete = reverse(
            "task_manager:task-type-delete", args=[task_type_delete.id]
        )
        response = self.client.post(url_to_delete)
        self.assertEqual(response.status_code, 302)


class SearchTaskTypeTests(TestCase):
    """test the task type search field on task_type llist"""

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test12345",
        )
        self.client.force_login(self.user)

    def test_task_type_search_field(self):
        response = self.client.get(
            reverse("task_manager:task-type-list") + "?name=test"
        )
        self.assertEqual(
            list(response.context["task_type_list"]),
            list(TaskType.objects.filter(name__icontains="test")),
        )
