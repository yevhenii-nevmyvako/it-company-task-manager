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


class PrivateTeamTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="qwer1234",
        )
        self.client.force_login(self.user)

    def test_team_open_with_login_user(self):
        """test to open team with login user"""
        response = self.client.get(TEAM_URL)

        self.assertEqual(response.status_code, 200)

    def test_create_team_open_with_login_user(self):
        """test client open create team with login user"""
        response = self.client.get(TEAM_URL)

        self.assertEqual(response.status_code, 200)

    def test_create_team_with_login_user(self):
        """test should create team with user"""
        Team.objects.create(name="test")
        response = self.client.get(TEAM_URL)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_team_detail_with_login_user(self):
        """test retrieved team detail page with login user"""
        team = Team.objects.create(
            name="test"
        )
        url_to_detail = reverse(
            "task_manager:team-detail", args=[team.id]
        )
        response = self.client.get(url_to_detail)

        self.assertEqual(response.status_code, 200)

    def test_retrieve_team_delete_with_login_user(self):
        """test retrieved project delete page with login user"""
        team = Team.objects.create(
            name="test"
        )
        url_to_delete = reverse(
            "task_manager:team-delete", args=[team.id]
        )
        response = self.client.get(url_to_delete)

        self.assertEqual(response.status_code, 200)

    def test_equal_team_list_queryset_with_login_user(self):
        """test equal team lists queryset with login user"""
        team_all = Team.objects.all()
        response = self.client.get(TEAM_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["team_list"]), list(team_all)
        )

    def test_retrieve_team_template_with_login_user(self):
        """test check team template with login user"""
        response = self.client.get(TEAM_URL)

        self.assertTemplateUsed(
            response, "task_manager/team_list.html"
        )

    def test_retrieve_template_team_form_with_login_user(self):
        """test retrieve template team_form.html"""
        response = self.client.get(TEAM_URL)

        self.assertTemplateUsed(
            response, "task_manager/team_list.html"
        )

    def test_retrieve_template_team_delete_confirm_with_login_user(self):
        """test retrieve template team_delete_confirm.html"""
        team = Team.objects.create(name="test")
        url_to_delete = reverse(
            "task_manager:team-delete", args=[team.id]
        )
        response = self.client.get(url_to_delete)

        self.assertTemplateUsed(
            response, "task_manager/team_delete_confirm.html"
        )

    def test_retrieve_template_team_detail_with_login_user(self):
        """test retrieve template team_detail.html"""
        team = Team.objects.create(name="test")
        url_to_detail = reverse(
            "task_manager:team-detail", args=[team.id]
        )
        response = self.client.get(url_to_detail)

        self.assertTemplateUsed(
            response, "task_manager/team_detail.html"
        )

    def test_delete_required_in_detail_team_with_login(self):
        """test should delete the team"""
        team_delete = Team.objects.create(
            name="test")
        url_to_delete = reverse(
            "task_manager:team-delete", args=[team_delete.id]
        )
        response = self.client.post(url_to_delete)
        self.assertEqual(response.status_code, 302)


class SearchTeamTests(TestCase):
    """test the team search field on team list"""

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test12345",
        )
        self.client.force_login(self.user)

    def test_team_search_field(self):
        response = self.client.get(
            reverse("task_manager:team-list") + "?name=test"
        )
        self.assertEqual(
            list(response.context["team_list"]),
            list(Team.objects.filter(name__icontains="test")),
            )
