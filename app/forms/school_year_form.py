from django import forms
from app.models import School_year
from django.forms import ModelForm


class AddSchoolYearForm(forms.ModelForm):
    year_from = forms.IntegerField(label='Year From')
    year_to = forms.IntegerField(label='Year To')

    class Meta:
        model = School_year
        fields = ['semester', 'year_from', 'year_to']
