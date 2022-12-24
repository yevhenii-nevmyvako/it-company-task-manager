from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.forms import WorkerCreationFrom, PositionForm, TaskTypeForm, CompletedForm
from task_manager.models import Position


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
