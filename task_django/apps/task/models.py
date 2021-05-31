from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime


class Course(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)

    def get_count_student(self):

        count = CourseParticipant.objects.filter(course=self.id)
        return len(count)

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def get_count_course(self):
        count = CourseParticipant.objects.filter(student=self.id)
        return len(count) if count else 0

    def get_count_ended_course(self):
        count = CourseParticipant.objects.filter(student=self.id, completed=True)
        return len(count) if count else 0

    def __str__(self):
        return f'{self.first_name}'


class CourseParticipant(models.Model):

    course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='student', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)




