from django.conf.urls import url
from app.views import index, student, event, school_year

urlpatterns = [
    url(r'^attendance/signout/(?P<pk>[0-9]+)/$', event.attendance_page_signout, name='attendance_page_sign_out'),
    url(r'^attendance/signin/(?P<pk>[0-9]+)/$', event.attendance_page_signin, name='attendance_page_sign_in'),
    url(r'^attendance/signout//log/(?P<pk>[0-9]+)/$', event.get_signout_log, name='view_attendance_log_signout'),
    url(r'^attendance/signin/log/(?P<pk>[0-9]+)/$', event.get_signin_log, name='view_attendance_log_signin'),
    url(r'^addevent/$', event.add_event, name='add_event'),
    url(r'^events/$', event.get_eventList, name='event_list'),
    url(r'^addstudent/$', student.add_student, name='add_student'),
    url(r'^studentlist/$', student.get_studentList, name='view_student'),
    url(r'^schoolyear/$', school_year.add_schoolyear, name='add_schoolyear'),
    url(r'', index.home, name='home'),
]