from django import forms
from django.forms import TextInput, Textarea, DateInput

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'course', 'description', 'start_date', 'end_date']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your firstname', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your lastname', 'class': 'form-control'}),
            'course': TextInput(attrs={'placeholder': 'Please enter your course', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

