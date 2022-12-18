# Generated by Django 4.1.3 on 2022-12-18 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("task_manager", "0007_alter_profile_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="id",
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="profiles",
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
