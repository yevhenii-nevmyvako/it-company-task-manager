from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import Task, Position


class ModelsTest(TestCase):

    def test_worker_str(self):
        """test __str__ method in worker model"""
        worker = get_user_model().objects.create_user(
            username="testname",
            password="test12345",
            first_name="Test First",
            last_name="Test Last"
        )
        self.assertEqual(
            str(worker), f"Username: {worker.username}"
                         f" Full name: ({worker.first_name}"
                         f" {worker.last_name})"
        )

    def test_task_str(self):
        """test __str__method in task model"""
        task = Task.objects.create(
            priority="Ugent",
            is_completed="True"
        )
        self.assertEqual(
            str(task), f" deadline date: {task.deadline}"
                       f" priority: {task.priority}"
                       f" is completed: {task.is_completed}"
        )

    def test_position_str(self):
        """test __str__method in position model"""
        position = Position.objects.create(
            name="test"
        )
        self.assertEqual(str(position), position.name)
