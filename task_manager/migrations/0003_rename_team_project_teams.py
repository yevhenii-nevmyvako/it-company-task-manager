# Generated by Django 4.1.3 on 2022-12-15 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "task_manager",
            "0002_project_team_alter_task_options_alter_worker_options_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="team",
            new_name="teams",
        ),
    ]