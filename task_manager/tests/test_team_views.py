from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Team

TEAM_URL = reverse("task_manager:team-list")
TEAM_CREATE_URL = reverse("task_manager:team-create")


class PublicTeamTests(TestCase):

    def test_team_open_list_required(self):
        """test login required in team
        list view doesn't work without login"""
        response = self.client.get(TEAM_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_create_team_login_required(self):
        """test client doesn't open create
        team without login required"""
        response = self.client.get(TEAM_CREATE_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_delete_team_login_required(self):
        """test doesn't open team_delete_confirm without login"""
        team = Team.objects.create(
            name="test"
        )
        url_to_delete = reverse(
            "task_manager:team-delete", args=[team.id]
        )
        response = self.client.get(url_to_delete)

        self.assertNotEqual(response.status_code, 200)

    def test_detail_team_login_required(self):
        """test doesn't open team_detail without login"""
        team = Team.objects.create(
            name="test"
        )
        url_to_detail = reverse(
            "task_manager:team-detail", args=[team.id]
        )
        response = self.client.get(url_to_detail)

        self.assertNotEqual(response.status_code, 200)

    def test_update_team_login_required(self):
        """test doesn't open team_form without login"""
        team = Team.objects.create(
            name="test"
        )
        url_to_update = reverse(
            "task_manager:team-update", args=[team.id]
        )
        response = self.client.get(url_to_update)

        self.assertNotEqual(response.status_code, 200)