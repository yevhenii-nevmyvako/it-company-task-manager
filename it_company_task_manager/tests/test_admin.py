from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from task_manager.models import Position


class AdminSiteTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="test12345"
        )
        self.client.force_login(self.admin_user)
        position = Position.objects.create(name="test")
        self.worker = get_user_model().objects.create_user(
            username="tests",
            password="tests1234",
            first_name="testing",
            last_name="testing",
            position=position
        )

    def test_worker_position_listed(self):
        """test that worker has position in list_display on worker admin page"""
        url = reverse("admin:task_manager_worker_changelist")
        # url = "http://127.0.0.1:8005/admin/task_manager/worker/"
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)
