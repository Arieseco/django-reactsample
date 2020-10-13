from django.shortcuts import render
from .models import Attendance
from rest_framework import generics
from .serializers import AttendanceSerializer
# Create your views here.

class AttendanceListAPIView(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
