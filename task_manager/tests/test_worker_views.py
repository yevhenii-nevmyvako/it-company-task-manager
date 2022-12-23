from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Worker, Position

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


class PrivateWorkerTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="qwer1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_worker_list_with_login(self):
        """test retrieved worker list with login required"""
        response = self.client.get(WORKER_URL)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_worker_create_with_login(self):
        """test retrieved worker create page with login required"""
        response = self.client.get(WORKER_CREATE_URL)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_worker_detail_with_login(self):
        """test retrieved worker detail page with login required"""
        worker_detail = Worker.objects.create(
            first_name="test", last_name="testing"
        )
        url_to_detail = reverse(
            "task_manager:worker-detail", args=[worker_detail.id]
        )
        response = self.client.get(url_to_detail)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_worker_delete_with_login(self):
        """test retrieved worker delete page with login required"""
        worker_detail = Worker.objects.create(first_name="test", last_name="testing")
        url_to_delete = reverse(
            "task_manager:worker-delete", args=[worker_detail.id]
        )
        response = self.client.get(url_to_delete)

        self.assertEqual(response.status_code, 200)

    def test_equal_worker_list_queryset_with_login(self):
        """test equal worker lists queryset with  login required"""
        workers_all = Worker.objects.all()
        response = self.client.get(WORKER_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["worker_list"]), list(workers_all)
        )

    def test_equal_worker_template_with_login(self):
        """test check worker template with login required"""
        response = self.client.get(WORKER_URL)

        self.assertTemplateUsed(response, "task_manager/worker_list.html")

    def test_equal_worker_create_template_with_login(self):
        """test check worker create template with login"""
        response = self.client.get(WORKER_CREATE_URL)

        self.assertTemplateUsed(response, "task_manager/worker_form.html")

    def test_create_worker_with_position(self):
        """test create worker with position"""
        position = Position.objects.create(name="test-position")
        Worker.objects.create(
            first_name="test",
            last_name="testing",
            position=position
        )
        response = self.client.get(WORKER_URL)
        self.assertEqual(response.status_code, 200)


class SearchWorkerTests(TestCase):
    """test the worker search field"""

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test12345",
        )
        self.client.force_login(self.user)

    def test_worker_search_field(self):
        response = self.client.get(
            reverse("task_manager:worker-list") + "?username=test"
        )
        self.assertEqual(
            list(response.context["worker_list"]),
            list(Worker.objects.filter(username__icontains="test")),
        )
