from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from app.models import *
from django.template import RequestContext
from app.forms.school_year_form import AddSchoolYearForm

def add_schoolyear(request):
    if request.method == 'POST':
        form = AddSchoolYearForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            add_form = AddSchoolYearForm()
            return render(request, "app/school_year/school_year.html", {'form': add_form, 'success': True})
        else:
            add_form = AddSchoolYearForm()
            return render(request, "app/school_year/school_year.html", {'form': add_form, 'error': True})
    add_form = AddSchoolYearForm()
    return render(request, "app/school_year/school_year.html", {'form': add_form})
