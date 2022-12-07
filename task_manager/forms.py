from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from task_manager.models import Worker, Task, Position


class WorkerCreationFrom(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "position",
        )


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]

        if not name.isalpha():
            raise ValidationError("Should be no digits in position field")
        return name


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


class WorkerPositionUpdateForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ("position",)


class PositionSearchForm(forms.Form):
    position = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by position"
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
