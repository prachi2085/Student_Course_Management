from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment
from django.contrib.auth.decorators import login_required
from rest_framework import generics
# from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer

class CourseListAPI(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentListAPI(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('course_detail', course_id=course.id)
