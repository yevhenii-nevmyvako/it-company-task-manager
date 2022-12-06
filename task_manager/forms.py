# from django import forms
from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Worker


class WorkerCreationFrom(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("position",)
