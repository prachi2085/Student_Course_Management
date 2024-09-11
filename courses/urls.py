from django.urls import path
from . import views
# from django.urls import path
# from . import views

urlpatterns = [
    path('api/courses/', views.CourseListAPI.as_view(), name='api_course_list'),
    path('api/enrollments/', views.EnrollmentListAPI.as_view(), name='api_enrollment_list'),
]


urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/enroll/', views.enroll_course, name='enroll_course'),
]
