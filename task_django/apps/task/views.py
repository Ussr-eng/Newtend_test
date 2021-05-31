from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from datetime import timedelta, datetime, date
from django.utils import timezone
from django.db.models import F, Q, When

import csv
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .models import Course, Student, CourseParticipant
from .serializers import StudentSerializer, CourseSerializer, CourseParticipantSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get_queryset(self):

        return self.queryset.all()

    def perform_create(self, serializer):

        serializer.save()

    def perform_update(self, serializer):

        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner')

        serializer.save()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):

        return self.queryset.all()

    def perform_create(self, serializer):

        serializer.save()

    def perform_update(self, serializer):

        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner')

        serializer.save()


class CourseParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = CourseParticipantSerializer
    queryset = CourseParticipant.objects.all()

    @action(detail=True, methods=['post', 'get'])
    def get_course_participant(self, request, pk=None):

        courses = CourseParticipant.objects.filter(course=pk)[:10]
        result = {}

        [result.update({list(result)[-1] + 1 if result else 1: item.student.__dict__}) for item in courses]
        [result[x].pop('_state') for x in range(1, len(result)+1)]

        return Response(result, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post', 'get'])
    def delete_participant(self, request, pk=None):

        course_participant = CourseParticipant.objects.filter(course=pk, student=request.data['course']).delete()

        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post', 'get'])
    def potential_participants(self, request, pk=None):

        potential = Student.objects.exclude(student__course=pk)

        serializer = StudentSerializer(potential, many=True)
        return Response([serializer.data], status=status.HTTP_200_OK)

    @action(detail=True, methods=['post', 'get'])
    def add_participant(self, request, pk=None):

        potential = CourseParticipant.objects.create(course_id=int(pk),
                                                     student_id=request.data['participant_id'])

        # serializer = StudentSerializer(potential, many=True)
        # return Response([serializer.data], status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

    def get_queryset(self):

        return self.queryset.filter()

    def perform_create(self, serializer):

        serializer.save()

    def perform_update(self, serializer):

        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner')

        serializer.save()


@api_view(['GET'])
def report_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="members.csv"'

    writer = csv.writer(response)
    students = Student.objects.all()

    [writer.writerow([f'Имя:{item.first_name} ', f'Фамилия: {item.last_name} ',
                      f'Почта: {item.email} ', f'Количество курсов: {item.get_count_course()} ',
                      f'Количество законченных курсов: {item.get_count_ended_course()} ']) for item in students]

    return response


