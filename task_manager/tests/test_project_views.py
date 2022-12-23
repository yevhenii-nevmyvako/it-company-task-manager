from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Project


PROJECT_URL = reverse("task_manager:project-list")
PROJECT_CREATE_URL = reverse("task_manager:project-create")


class PublicProjectTests(TestCase):

    def test_project_open_list_required(self):
        """test login required in project
        list view doesn't work without login"""
        response = self.client.get(PROJECT_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_create_project_login_required(self):
        """test client doesn't open create
        project without login required"""
        response = self.client.get(PROJECT_CREATE_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_delete_project_login_required(self):
        """test doesn't open project_delete_confirm without login"""
        project = Project.objects.create(
            name="test"
        )
        url_to_delete = reverse(
            "task_manager:project-delete", args=[project.id]
        )
        response = self.client.get(url_to_delete)

        self.assertNotEqual(response.status_code, 200)

    def test_detail_project_login_required(self):
        """test doesn't open project_detail without login"""
        project = Project.objects.create(
            name="test"
        )
        url_to_detail = reverse(
            "task_manager:project-detail", args=[project.id]
        )
        response = self.client.get(url_to_detail)

        self.assertNotEqual(response.status_code, 200)

    def test_update_project_login_required(self):
        """test doesn't open project_form without login"""
        project = Project.objects.create(
            name="test"
        )
        url_to_update = reverse(
            "task_manager:project-update", args=[project.id]
        )
        response = self.client.get(url_to_update)

        self.assertNotEqual(response.status_code, 200)


class PrivateProjectTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="qwer1234"
        )
        self.client.force_login(self.user)

    def test_project_open_with_login_required(self):
        """test to open task project with login required"""
        response = self.client.get(PROJECT_URL)

        self.assertEqual(response.status_code, 200)

    def test_create_project_open_with_login_required(self):
        """test client open create project with login required"""
        response = self.client.get(PROJECT_CREATE_URL)

        self.assertEqual(response.status_code, 200)

    def test_create_project_with_login_required(self):
        """test should create project with user login"""
        Project.objects.create(name="test")
        response = self.client.get(PROJECT_CREATE_URL)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_project_detail_with_login(self):
        """test retrieved project detail page with login required"""
        project = Project.objects.create(
            name="test"
        )
        url_to_detail = reverse(
            "task_manager:project-detail", args=[project.id]
        )
        response = self.client.get(url_to_detail)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_project_delete_with_login(self):
        """test retrieved project delete page with login required"""
        project = Project.objects.create(
            name="test"
        )
        url_to_delete = reverse(
            "task_manager:project-delete", args=[project.id]
        )
        response = self.client.get(url_to_delete)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_project_update_with_login(self):
        """test retrieved project delete page with login required"""
        project = Project.objects.create(
            name="test"
        )
        url_to_update = reverse(
            "task_manager:project-update", args=[project.id]
        )
        response = self.client.get(url_to_update)

        self.assertEqual(response.status_code, 200)

    def test_equal_project_list_queryset_with_login(self):
        """test equal project lists queryset with login required"""
        project_all = Project.objects.all()
        response = self.client.get(PROJECT_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["project_list"]), list(project_all)
        )

    def test_retrieve_project_template_with_login(self):
        """test check project template with login required"""
        response = self.client.get(PROJECT_URL)

        self.assertTemplateUsed(
            response, "task_manager/project_list.html"
        )

    def test_retrieve_template_project_form_with_login(self):
        """test retrieve template project_form.html"""
        response = self.client.get(PROJECT_CREATE_URL)

        self.assertTemplateUsed(
            response, "task_manager/project_form.html"
        )

    def test_retrieve_template_project_delete_confirm_with_login(self):
        """test retrieve template project_delete_confirm.html"""
        project = Project.objects.create(name="test")
        url_to_delete = reverse(
            "task_manager:project-delete", args=[project.id]
        )
        response = self.client.get(url_to_delete)

        self.assertTemplateUsed(
            response, "task_manager/project_delete_confirm.html"
        )

    def test_retrieve_template_project_detail_with_login(self):
        """test retrieve template project_detail.html"""
        project = Project.objects.create(name="test")
        url_to_detail = reverse(
            "task_manager:project-detail", args=[project.id]
        )
        response = self.client.get(url_to_detail)

        self.assertTemplateUsed(
            response, "task_manager/project_detail.html"
        )

    def test_retrieve_template_project_update_with_login(self):
        """test retrieve template project_form.html"""
        project = Project.objects.create(name="test")
        url_to_update = reverse(
            "task_manager:project-update", args=[project.id]
        )
        response = self.client.get(url_to_update)

        self.assertTemplateUsed(
            response, "task_manager/project_form.html"
        )
