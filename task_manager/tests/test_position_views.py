from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


POSITION_URL = reverse("task_manager:position-list")
POSITION_CREATE_URL = reverse("task_manager:position-create")


class PublicPositionTests(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_position_login_list_required(self):
        """test login required in position list view doesn't work without login"""
        response = self.client.get(POSITION_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_create_position_create_login_required(self):
        """test client doesn't open create position without login required"""
        response = self.client.get(POSITION_CREATE_URL)
        self.assertNotEqual(response.status_code, 200)
