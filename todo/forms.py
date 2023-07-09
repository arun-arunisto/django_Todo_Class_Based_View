from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        def __init__(self, *args, **kwargs):
            super(TodoForm, self).__init__(*args, **kwargs)
            self.fields['title'].widget.attrs = {
                'class': 'form-control col-md-6'
            }
            self.fields['description'].widget.attrs = {
                'class': 'form-control col-md-6'
            }
        model = Todo
        fields = ['title', 'description']