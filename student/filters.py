import django_filters
from django import forms
from django_filters import DateFilter

from student.models import Student


class StudentFilter(django_filters.FilterSet):
    # exact, istartswith, iendswith, iconteains
    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name')
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')

    # gte -> greater than or equal to, lte -> less than or equal to, gt -> greater then, lt -> less then.

    start_date_gte = DateFilter(field_name='start_date', label='From start date', lookup_expr='gte',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    start_date_lte = DateFilter(field_name='start_date', label='To start date', lookup_expr='lte',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    end_date_gte = DateFilter(field_name='end_date', label='From end date', lookup_expr='gte',
                              widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date_lte = DateFilter(field_name='end_date', label='To end date', lookup_expr='lte',
                              widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'is_olympic', 'start_date_gte', 'start_date_lte',
                  'end_date_gte', 'end_date_lte', 'trainer']

    def __init__(self, *args, **kwargs):
        super(StudentFilter, self).__init__(*args, **kwargs)

        self.filters['first_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a first name'})
        self.filters['last_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a last name'})
        self.filters['age'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter an age'})
        self.filters['is_olympic'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['trainer'].field.widget.attrs.update({'class': 'form-select'})

