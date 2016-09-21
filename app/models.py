from datetime import time
import django
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# CUSTOM USER AUTH
###############################################################################

class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email,
            is_superuser=True,
            is_staff=True,
            is_active=True,
            is_admin=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return UserManager


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    contact_number = models.CharField(max_length=30, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    objects = UserManager()


###############################################################################
###############################################################################
###############################################################################

class Student(models.Model):
    YEAR_LIST = [
        (1, '1st'),
        (2, '2nd'),
        (3, '3rd'),
        (4, '4th'),
    ]

    id_number = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_initial = models.CharField(max_length=3)
    year_level = models.IntegerField(choices=YEAR_LIST)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    is_active = models.BooleanField(default=True)

    def get_fullName(self):
        return self.last_name + ', ' + self.first_name + ' ' + self.middle_initial + '.'

    def get_firstName(self):
        return self.first_name

    def get_lastName(self):
        return self.last_name

    def get_yearLevel(self):
        return self.year_level

    def student_info(self):
        info = {
            'fullName': self.get_fullName(),
            'firstName': self.first_name,
            'middleInitial': self.middle_initial,
            'lastName': self.last_name,
            'yearLevel': self.year_level,
            'date_created': self.date_created
        }
        return info


class School_year(models.Model):
    SEM_LIST = (
        (1, '1st'),
        (2, '2nd'),
        (3, 'Summer'),
    )
    semester = models.IntegerField(choices=SEM_LIST)
    year_from = models.IntegerField()
    year_to = models.IntegerField()
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.year_from) + " - " + str(self.year_to)

    def get_semester(self):
        return str(self.semester) + " Semester"


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    school_year = models.ForeignKey(School_year)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    is_active = models.BooleanField(default=True)


class Attendance(models.Model):
    student = models.ForeignKey(Student)
    event = models.ForeignKey(Event)
    is_present = models.BooleanField(default=True)
    type = models.IntegerField()
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    is_active = models.BooleanField(default=True)
