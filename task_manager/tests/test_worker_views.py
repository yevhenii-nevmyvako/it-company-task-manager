from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from task_manager.models import Worker

WORKER_URL = reverse("task_manager:worker-list")
WORKER_CREATE_URL = reverse("task_manager:worker-create")


class PublicWorkerTests(TestCase):

    def test_login_required_worker(self):
        """test login required in worker list view"""
        response = self.client.get(WORKER_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_create_worker_not_required(self):
        """test create worker without login required"""
        response = self.client.get(WORKER_CREATE_URL)

        self.assertEqual(response.status_code, 200)

    # def test_login_required_worker_detail(self):
    #     """test login required in worker detail view"""
    #     response = self.client.get(WORKER_DETAIL_URL)
    #
    #     self.assertNotEqual(response.status_code, 200)
