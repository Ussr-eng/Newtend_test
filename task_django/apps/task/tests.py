import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .serializers import StudentSerializer, CourseSerializer, CourseParticipantSerializer
from .models import CourseParticipant, Student, Course
from django.test import TestCase
