from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from task_manager.models import Position

POSITION_URL = reverse("task_manager:position-list")
POSITION_CREATE_URL = reverse("task_manager:position-create")


class PublicPositionTests(TestCase):

    def test_position_open_list_required(self):
        """test login required in position
        list view doesn't work without login"""
        response = self.client.get(POSITION_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_create_position_login_required(self):
        """test client doesn't open create
        position without login required"""
        response = self.client.get(POSITION_CREATE_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivatePositionTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="qwer1234"
        )
        self.client.force_login(self.user)

    def test_position_open_with_login_required(self):
        """test to open position list with login required"""
        response = self.client.get(POSITION_URL)

        self.assertEqual(response.status_code, 200)

    def test_create_position_open_with_login_required(self):
        """test client open create position with login required"""
        response = self.client.get(POSITION_CREATE_URL)

        self.assertEqual(response.status_code, 200)

    def test_create_position_with_login_required(self):
        """test should create position with user login"""
        Position.objects.create(name="test")
        response = self.client.get(POSITION_CREATE_URL)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_position_detail_with_login(self):
        """test retrieved position detail page with login required"""
        worker_position = Position.objects.create(
            name="test"
        )
        url_to_detail = reverse(
            "task_manager:position-detail", args=[worker_position.id]
        )
        response = self.client.get(url_to_detail)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_position_delete_with_login(self):
        """test retrieved position delete page with login required"""
        worker_position = Position.objects.create(
            name="test"
        )
        url_to_delete = reverse(
            "task_manager:position-delete", args=[worker_position.id]
        )
        response = self.client.get(url_to_delete)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_position_update_with_login(self):
        """test retrieved position delete page with login required"""
        worker_position = Position.objects.create(
            name="test"
        )
        url_to_update = reverse(
            "task_manager:position-update", args=[worker_position.id]
        )
        response = self.client.get(url_to_update)

        self.assertEqual(response.status_code, 200)

    def test_equal_position_list_queryset_with_login(self):
        """test equal worker lists queryset with  login required"""
        position_all = Position.objects.all()
        response = self.client.get(POSITION_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["position_list"]), list(position_all)
        )



