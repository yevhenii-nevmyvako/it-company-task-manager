from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Project, Task, TaskType

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


class PrivateTaskTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="qwer1234",
        )
        self.client.force_login(self.user)
        self.task_type = TaskType.objects.create(name="test1")
        self.projects = Project.objects.create(name="test2")

    def test_task_open_with_login_user(self):
        """test to open task with login user"""
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)

    def test_create_task_open_with_login_user(self):
        """test client open create task with login user"""
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)

    def test_create_task_task_type_with_login_user(self):
        """test should create task with task_type"""
        Task.objects.create(
            task_type=self.task_type
        )
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)

    def test_create_task_project_with_login_user(self):
        """test should create task with project"""
        Task.objects.create(
            projects=self.projects
        )
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_task_detail_with_login_user(self):
        """test retrieved task detail page with login user"""
        task = Task.objects.create(
            task_type=self.task_type
        )
        url_to_detail = reverse(
            "task_manager:task-detail", args=[task.id]
        )
        response = self.client.get(url_to_detail)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_task_delete_with_login_user(self):
        """test retrieved task delete page with login user"""
        task = Task.objects.create(
            task_type=self.task_type
        )
        url_to_delete = reverse(
            "task_manager:task-delete", args=[task.id]
        )
        response = self.client.get(url_to_delete)

        self.assertEqual(response.status_code, 200)

    def test_equal_task_list_queryset_with_login_user(self):
        """test equal task lists queryset with login user"""
        task_all = Task.objects.all()
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]), list(task_all)
        )

    def test_retrieve_task_template_with_login_user(self):
        """test check task template with login user"""
        response = self.client.get(TASK_URL)

        self.assertTemplateUsed(
            response, "task_manager/task_list.html"
        )

    def test_retrieve_template_task_form_with_login_user(self):
        """test retrieve template task_form.html"""
        response = self.client.get(TASK_URL)

        self.assertTemplateUsed(
            response, "task_manager/task_list.html"
        )

    def test_retrieve_template_task_delete_confirm_with_login_user(self):
        """test retrieve template task_delete_confirm.html"""
        task = Task.objects.create(task_type=self.task_type)
        url_to_delete = reverse(
            "task_manager:task-delete", args=[task.id]
        )
        response = self.client.get(url_to_delete)

        self.assertTemplateUsed(
            response, "task_manager/task_delete_confirm.html"
        )

    def test_retrieve_template_task_detail_with_login_user(self):
        """test retrieve template task_detail.html"""
        task = Task.objects.create(task_type=self.task_type)
        url_to_detail = reverse(
            "task_manager:task-detail", args=[task.id]
        )
        response = self.client.get(url_to_detail)

        self.assertTemplateUsed(
            response, "task_manager/task_detail.html"
        )

    def test_delete_required_in_detail_task_with_login(self):
        """test should delete the task"""
        task_delete = Task.objects.create(
            task_type=self.task_type)
        url_to_delete = reverse(
            "task_manager:task-delete", args=[task_delete.id]
        )
        response = self.client.post(url_to_delete)
        self.assertEqual(response.status_code, 302)


class SearchTaskTests(TestCase):
    """test the task search field on team list"""

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test12345",
        )
        self.client.force_login(self.user)

    def test_task_search_field(self):
        response = self.client.get(
            reverse("task_manager:task-list") + "?task_type=test"
        )
        self.assertEqual(
            list(response.context["task_list"]),
            list(Task.objects.filter(task_type__name__icontains="test")),
            )
