from django import forms
from app.models import Student
from django.forms import ModelForm


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id_number', 'first_name', 'last_name', 'middle_initial',
                  'year_level'
                  ]
