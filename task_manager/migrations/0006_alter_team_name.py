# Generated by Django 4.1.3 on 2022-12-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_manager", "0005_alter_team_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
