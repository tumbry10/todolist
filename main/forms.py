from django import forms
from .models import Task, TaskCartegory

class TaskCartegoryCreationForm(forms.ModelForm):
    class Meta:
        model = TaskCartegory
        fields = ('name',)


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

