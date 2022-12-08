# Generated by Django 4.1.3 on 2022-12-08 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("task_manager", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["deadline"]},
        ),
        migrations.AlterModelOptions(
            name="worker",
            options={
                "ordering": ["username"],
                "verbose_name": "Worker",
                "verbose_name_plural": "Workers",
            },
        ),
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(blank=True, null=True),
        ),
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
        migrations.AlterField(
            model_name="worker",
            name="position",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="workers",
                to="task_manager.position",
            ),
        ),
        migrations.AddConstraint(
            model_name="team",
            constraint=models.UniqueConstraint(
                fields=("name",), name="unique_team_name"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="teams",
            field=models.ManyToManyField(
                null=True, related_name="projects", to="task_manager.team"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="project",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="task_manager.project",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="worker",
            name="team",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="workers",
                to="task_manager.team",
            ),
        ),
        migrations.AddConstraint(
            model_name="project",
            constraint=models.UniqueConstraint(
                fields=("name",), name="unique_project_name"
            ),
        ),
    ]