from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import Task, Position, TaskType, Team, Project


class ModelsTest(TestCase):

    def test_worker_str(self) -> None:
        """test __str__ method in worker model"""
        position = Position.objects.create(name="test")
        worker = get_user_model().objects.create_user(
            username="testname",
            password="test12345",
            first_name="Test First",
            last_name="Test Last",
            position=position
        )
        self.assertEqual(
            str(worker), f"Username: {worker.username}"
                         f" | Full name: ({worker.first_name}"
                         f" {worker.last_name})"
                         f" Position: {worker.position}"

        )

    def test_task_str(self) -> None:
        """test __str__ method in task model"""
        task_type = TaskType.objects.create(name="test")
        projects = Project.objects.create(name="test")
        task = Task.objects.create(
            priority="Ugent",
            is_completed="True",
            task_type=task_type,
            projects=projects
        )
        self.assertEqual(
            str(task), f"task type: {task.task_type.name}"
                       f" deadline date: {task.deadline}"
                       f" priority: {task.priority}"
                       f" is completed: {task.is_completed}"
                       f" project: {task.projects.name}"
        )

    def test_position_str(self) -> None:
        """test __str__ method in position model"""
        position = Position.objects.create(
            name="test"
        )
        self.assertEqual(str(position), position.name)

    def test_task_type_str(self) -> None:
        """test __str__ method in tasktype model"""
        task_type = TaskType.objects.create(
            name="test"
        )
        self.assertEqual(str(task_type), task_type.name)

    def test_team_str(self) -> None:
        """test __str__ method in team model"""
        team = Team.objects.create(
            name="test"
        )
        self.assertEqual(str(team), team.name)

    def test_project_str(self) -> None:
        """test __str__ method in project model"""
        project = Project.objects.create(
            name="test"
        )
        self.assertEqual(str(project), project.name)
