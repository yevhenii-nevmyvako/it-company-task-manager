from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import Task


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
        """Should test __str__method in task model"""
        task = Task.objects.crate(

            f"Task type: {self.task_type.name}"
            f" (deadline date: {self.deadline},"
            f" priority: {self.priority}"

        )




