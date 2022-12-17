# Generated by Django 4.1.3 on 2022-12-16 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("task_manager", "0003_rename_team_project_teams"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="tasks",
        ),
        migrations.AddField(
            model_name="task",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Tasks",
                to="task_manager.project",
            ),
        ),
    ]