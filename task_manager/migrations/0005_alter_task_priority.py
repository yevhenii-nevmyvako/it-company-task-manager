# Generated by Django 4.1.3 on 2022-12-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_manager", "0004_alter_worker_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[
                    ("ugent", "Ugent priority task"),
                    ("high", "High priority task"),
                    ("medium", "Medium priority task"),
                    ("low", "Low priority task"),
                    ("lowest", "Lowest priority task"),
                ],
                max_length=6,
            ),
        ),
    ]