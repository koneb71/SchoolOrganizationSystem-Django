from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import *
from app.forms.student_form import AddStudentForm

def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            add_student_form = AddStudentForm()
            return render(request, "app/student/add_student.html", {'form': add_student_form, 'success': True})
        else:
            add_student_form = AddStudentForm()
            return render(request, "app/student/add_student.html", {'form': add_student_form, 'error': True})
    add_student_form = AddStudentForm()
    return render(request, "app/student/add_student.html", {'form': add_student_form})


def get_studentList(request):
    students = Student.objects.filter(is_active=True).order_by('last_name').order_by('year_level').all()
    paginator = Paginator(students, 8)

    page = request.GET.get('page')
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lists = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lists = paginator.page(paginator.num_pages)

    return render(request, 'app/student/view_students.html', {'lists': lists})