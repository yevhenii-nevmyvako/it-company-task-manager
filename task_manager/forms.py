from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Worker, Task


class WorkerCreationFrom(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "position",)


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        label="Deadline datetime",
        widget=forms.DateInput(
            format='%d-%m-%Y', attrs={'type': 'date'}
        )
        , required=False
    )
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"

