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
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)

    def test_worker_detailed_position_listed(self):
        """test that worker has position in worker detail admin page"""
        url = reverse("admin:task_manager_worker_change", args=[self.worker.id])
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)
