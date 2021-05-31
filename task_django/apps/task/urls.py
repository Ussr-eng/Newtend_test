from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseParticipantViewSet, CourseViewSet, StudentViewSet, report_csv

router = DefaultRouter()
router.register("course_participant", CourseParticipantViewSet, basename="course_participant")
router.register("course", CourseViewSet, basename="course")
router.register("student", StudentViewSet, basename="student")

urlpatterns = [
    path('', include(router.urls)),
    path('report_csv/', report_csv, name='report_csv')
]
