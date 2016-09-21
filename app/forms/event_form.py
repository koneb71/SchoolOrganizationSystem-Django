from django import forms
from app.models import Event, School_year, Attendance
from django.forms import ModelForm


class AddEventForm(forms.ModelForm):
    school_year = forms.ModelChoiceField(label = "School Year", queryset=School_year.objects.order_by('year_from').all(), widget=forms.Select)
    date = forms.DateField(
        widget= forms.SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        ),
    )
    class Meta:
        model = Event
        fields = ['name', 'date', 'school_year']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'event', 'is_present', 'type']
