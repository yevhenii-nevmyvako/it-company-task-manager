from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from task_manager.models import Worker, Task, Position, Team, Project, Profile


class WorkerCreationFrom(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "email", "position"
        )


class TeamForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Team
        fields = "__all__"


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]

        if [el for el in name if el in "0123456789"]:
            raise ValidationError("Should be no digits in position field")
        return name


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        label="Deadline datetime",
        widget=forms.DateInput(
            format='%d-%m-%Y', attrs={'type': 'date'}
        ),
        required=False
    )
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"


class CompletedForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("is_completed",)


class DeadlineForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("deadline",)


class PriorityForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("priority",)


class WorkerPositionUpdateForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ("position",)


class ProjectForm(forms.ModelForm):
    teams = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    # tasks = forms.ModelMultipleChoiceField(
    #     queryset=Task.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )

    class Meta:
        model = Project
        fields = "__all__"


class TeamWorkerUpdateForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ("members",)


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )


class TaskSearchForm(forms.Form):
    task_type = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by task type"
            }
        )
    )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


class ProjectSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


class TeamSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )
