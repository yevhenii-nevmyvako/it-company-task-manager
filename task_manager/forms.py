from django import forms
from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Worker, Task


class WorkerCreationFrom(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "position",)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"

