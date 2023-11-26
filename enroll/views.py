from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student, School
from .serializers import StudentSerializer, SchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
