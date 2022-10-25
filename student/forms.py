from django import forms
from django.forms import TextInput, EmailInput, Textarea, DateInput, Select

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'age', 'is_olympic',
                  'email', 'description', 'start_date', 'end_date', 'trainer']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your firstname', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your lastname', 'class': 'form-control'}),
            'age': TextInput(attrs={'placeholder': 'Please enter your age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trainer': Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data  # aici va fi un dictionar cu toate valorile introduse in formular
        all_students = Student.objects.all()  # interogam baza de date unde veti stoca toti studentii salvati in DB
        for student in all_students:  # iterez fiecare student salvat in DB
            if student.first_name == cleaned_data['first_name'] and student.last_name == cleaned_data['last_name']:
                msg = f'This first name {cleaned_data["first_name"]} ' \
                      f'and this last name {cleaned_data["last_name"]} exist in DB.'
                self._errors['first_name'] = self.error_class([msg])

        if cleaned_data['start_date'] > cleaned_data['end_date']:
            msg = f'The start date is older than the end date'
            self.errors['start_date'] = self.error_class([msg])

        return cleaned_data
