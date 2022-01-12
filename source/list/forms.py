from django import forms
from list.models import status_choices
from django.forms import widgets

class TaskForm(forms.Form):
    description = forms.CharField(max_length=1000, required=True, label='Описание')
    status = forms.ChoiceField(choices=status_choices, required=True, label='Статус', initial=status_choices[0][1])
    date = forms.DateField(required=False, label='Дедлайн', widget=widgets.DateTimeInput(attrs={"type": "date"}))
    detail = forms.CharField(max_length=2000, required=False, label='Подробное описание')

