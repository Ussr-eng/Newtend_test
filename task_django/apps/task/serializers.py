from rest_framework import serializers
from .models import Course, Student, CourseParticipant


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
        )


class CourseSerializer(serializers.ModelSerializer):

    get_count_student = serializers.IntegerField(required=False)

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "description",
            "start_date",
            "end_date",
            "get_count_student",
        )


class CourseParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseParticipant
        fields = (
            "id",
            "course",
            "student",
            "completed",
        )

    def to_representation(self, instance):

        self.fields['course'] = CourseSerializer(read_only=True)
        self.fields['student'] = StudentSerializer(read_only=True)

        return super(CourseParticipantSerializer, self).to_representation(instance)
