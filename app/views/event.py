from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from app.models import *
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.forms.event_form import AddEventForm, AttendanceForm

def add_event(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            add_form = AddEventForm()
            return render(request, "app/event/add_event.html", {'form': add_form, 'success': True})
        else:
            add_form = AddEventForm()
            return render(request, "app/event/add_event.html", {'form': add_form, 'error': True})
    add_form = AddEventForm()
    return render(request, "app/event/add_event.html", {'form': add_form})

def get_eventList(request):
    events = Event.objects.filter(is_active=True).order_by('date_created').all()
    return render(request, 'app/event/event_list.html', {'lists': events})


def attendance_page_signin(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        data = {
            'student': request.POST['id_number'],
            'event': event.id,
            'is_present': True,
            'type': int(''.join(request.POST['type']))
        }
        attendance = AttendanceForm(data)
        if attendance.is_valid():
            if data in Attendance.objects.all():
                attendance_log = Attendance.objects.filter(is_active=True, event=event, type=1).all()
                return render(request, "app/event/attendance-sign_in.html", {'list': event, 'log': attendance_log,
                                                                     'already_present': True,
                                                                             })
            else:
                attendance.save()
                attendance_log = Attendance.objects.filter(is_active=True, event=event, type=1).all()
                student_id = Student.objects.get(id_number=request.POST['id_number'])
                return render(request, "app/event/attendance-sign_in.html", {'list': event, 'log': attendance_log,
                                                                     'success': True, 'student': student_id})
        else:
            attendance_log = Attendance.objects.filter(is_active=True, event=event, type=1).all()
            return render(request, "app/event/attendance-sign_in.html",
                          {'list': event, 'log': attendance_log, 'error': True})

    attendance_log = Attendance.objects.filter(is_active=True, event=event, type=1).all()
    return render(request, "app/event/attendance-sign_in.html", {'list': event, 'log': attendance_log})


def attendance_page_signout(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        data = {
            'student': request.POST['id_number'],
            'event': event.id,
            'is_present': True,
            'type': int(''.join(request.POST['type']))
        }
        attendance = AttendanceForm(data)
        if attendance.is_valid():
            if data in Attendance.objects.filter(event=event).all():
                attendance_log = Attendance.objects.filter(is_active=True, event=event, type=2).all()
                return render(request, "app/event/attendance-sign_out.html", {'list': event, 'log': attendance_log,
                                                                     'already_present': True,
                                                                             })
            else:
                attendance.save()
                attendance_log = Attendance.objects.filter(is_active=True, event=event, type=2).all()
                student_id = Student.objects.get(id_number=request.POST['id_number'])
                return render(request, "app/event/attendance-sign_out.html", {'list': event, 'log': attendance_log,
                                                                     'success': True, 'student': student_id})
        else:
            attendance_log = Attendance.objects.filter(is_active=True, event=event, type=2).all()
            return render(request, "app/event/attendance-sign_out.html",
                          {'list': event, 'log': attendance_log, 'error': True})

    attendance_log = Attendance.objects.filter(is_active=True, event=event, type=2).all()
    return render(request, "app/event/attendance-sign_out.html", {'list': event, 'log': attendance_log})

def get_signin_log(request, pk):
    students = Attendance.objects.filter(is_active=True, event=pk, type=1).all()
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

    return render(request, 'app/event/view_attendance_log.html', {'lists': lists})

def get_signout_log(request, pk):
    students = Attendance.objects.filter(is_active=True, event=pk, type=2).all()
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

    return render(request, 'app/event/view_attendance_log.html', {'lists': lists})