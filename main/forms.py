

from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('task', 'due_date', 'user', 'done', 'details')

    class Done:
        done = forms.BooleanField()