from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Project


PROJECT_URL = reverse("task_manager:project-list")
PROJECT_CREATE_URL = reverse("task_manager:task-type-create")


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
