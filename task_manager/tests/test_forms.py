from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.forms import (
    PositionForm,
    TaskTypeForm,
    CompletedForm,
    PriorityForm
)

from task_manager.models import TaskType, Project


class TaskTypeFormTests(TestCase):

    def test_task_type_form(self):
        """test should validate task type form field"""
        form_data = {"name": "test"}
        form = TaskTypeForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_equal_task_type_form(self):
        """test should equal task type form field"""
        form_data = {"name": "test"}
        form = TaskTypeForm(data=form_data)
        form.is_valid()
        self.assertEqual(form.cleaned_data, form_data)


class PositionFormTests(TestCase):

    def test_position_form(self):
        """test should validate position field"""
        form_data = {"name": "test"}
        form = PositionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_equal_position_form(self):
        """test should equal position field"""
        form_data = {"name": "test"}
        form = PositionForm(data=form_data)
        form.is_valid()
        self.assertEqual(form.cleaned_data, form_data)


class CompletedFormTests(TestCase):

    def test_completed_form(self):
        """test should validate complete field"""
        form_data = {"is_completed": "True"}
        form = CompletedForm(data=form_data)
        self.assertTrue(form.is_valid())


class PriorityFormTests(TestCase):

    def test_priority_field_form(self):
        """test should validate priority field"""
        form_data = {"priority": "Ugent"}
        form = PriorityForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_equal_priority_field_form(self):
        """test should equal priority field"""
        form_data = {"priority": "Ugent"}
        form = PriorityForm(data=form_data)
        form.is_valid()
        self.assertEqual(form.cleaned_data, form_data)


class TaskFormTests(TestCase):

    def setUp(self) -> None:
        self.task_type = TaskType.objects.create(name="test")
        self.project = Project.objects.create(name="test project")
        self.assignees = get_user_model().objects.create_user(
            username="user_test",
            password="test2134",
            first_name="Test first",
            last_name="Test last",
        )
        self.client.force_login(self.assignees)

    def test_task_creation_form_with_position_assignees_task_type(self):
        """test should create task form with position & task type &assignees"""
        task = {
            "is_completed": "True",
            "priority": "Ugent",
            "task_type": self.task_type.id,
            "assignees": self.assignees.id,
            "project": self.project.id
        }
        response = self.client.post(reverse("task_manager:task-create"), task)
        self.assertEqual(response.status_code, 200)
