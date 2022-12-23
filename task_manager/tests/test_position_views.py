from django.contrib.auth import get_user_model
from django.test import TestCase
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

    def test_delete_task_type_login_required(self):
        """test doesn't open position_delete_confirm without login"""
        position = Position.objects.create(
            name="test"
        )
        url_to_delete = reverse(
            "task_manager:position-delete", args=[position.id]
        )
        response = self.client.get(url_to_delete)

        self.assertNotEqual(response.status_code, 200)

    def test_detail_task_type_login_required(self):
        """test doesn't open position_detail without login"""
        position = Position.objects.create(
            name="test"
        )
        url_to_detail = reverse(
            "task_manager:position-detail", args=[position.id]
        )
        response = self.client.get(url_to_detail)

        self.assertNotEqual(response.status_code, 200)

    def test_update_task_type_login_required(self):
        """test doesn't open task_type_form without login"""
        position = Position.objects.create(
            name="test"
        )
        url_to_update = reverse(
            "task_manager:position-update", args=[position.id]
        )
        response = self.client.get(url_to_update)

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
        position = Position.objects.create(
            name="test"
        )
        url_to_detail = reverse(
            "task_manager:position-detail", args=[position.id]
        )
        response = self.client.get(url_to_detail)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_position_delete_with_login(self):
        """test retrieved position delete page with login required"""
        position = Position.objects.create(
            name="test"
        )
        url_to_delete = reverse(
            "task_manager:position-delete", args=[position.id]
        )
        response = self.client.get(url_to_delete)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_position_update_with_login(self):
        """test retrieved position delete page with login required"""
        position = Position.objects.create(
            name="test"
        )
        url_to_update = reverse(
            "task_manager:position-update", args=[position.id]
        )
        response = self.client.get(url_to_update)

        self.assertEqual(response.status_code, 200)

    def test_equal_position_list_queryset_with_login(self):
        """test equal position lists queryset with login required"""
        position_all = Position.objects.all()
        response = self.client.get(POSITION_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["position_list"]), list(position_all)
        )

    def test_retrieve_position_template_with_login(self):
        """test check position template with login required"""
        response = self.client.get(POSITION_URL)

        self.assertTemplateUsed(response, "task_manager/position_list.html")

    def test_retrieve_template_position_form_with_login(self):
        """test retrieve template position_form.html"""
        response = self.client.get(POSITION_CREATE_URL)

        self.assertTemplateUsed(response, "task_manager/position_form.html")

    def test_retrieve_template_position_delete_confirm_with_login(self):
        """test retrieve template position_delete_confirm.html"""
        position = Position.objects.create(name="test")
        url_to_delete = reverse(
            "task_manager:position-delete", args=[position.id]
        )
        response = self.client.get(url_to_delete)

        self.assertTemplateUsed(response, "task_manager/position_delete_confirm.html")

    def test_retrieve_template_position_detail_with_login(self):
        """test retrieve template position_detail.html"""
        position = Position.objects.create(name="test")
        url_to_detail = reverse(
            "task_manager:position-detail", args=[position.id]
        )
        response = self.client.get(url_to_detail)

        self.assertTemplateUsed(response, "task_manager/position_detail.html")

    def test_retrieve_template_position_update_with_login(self):
        """test retrieve template position_form.html"""
        position = Position.objects.create(name="test")
        url_to_update = reverse(
            "task_manager:position-update", args=[position.id]
        )
        response = self.client.get(url_to_update)

        self.assertTemplateUsed(response, "task_manager/position_form.html")

    def test_delete_required_in_detail_position_with_login(self):
        """test should delete the position"""
        position_delete = Position.objects.create(
            name="test")
        url_to_delete = reverse(
            "task_manager:position-delete", args=[position_delete.id]
        )
        response = self.client.post(url_to_delete)
        self.assertEqual(response.status_code, 302)


class SearchPositionTests(TestCase):
    """test the position search field on position llist"""

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test12345",
        )
        self.client.force_login(self.user)

    def test_position_search_field(self):
        response = self.client.get(
            reverse("task_manager:position-list") + "?name=test"
        )
        self.assertEqual(
            list(response.context["position_list"]),
            list(Position.objects.filter(name__icontains="test")),
        )
