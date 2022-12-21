# Generated by Django 4.1.3 on 2022-12-21 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("task_manager", "0014_alter_project_teams"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="assignees",
            field=models.ManyToManyField(
                related_name="tasks", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="task_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="task_manager.tasktype",
            ),
        ),
    ]