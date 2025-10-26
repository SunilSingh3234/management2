from rest_framework import viewsets
from .models import Branch, Student, Subject, Marks, Attendance, Exam
from .serializers import BranchSerializer, StudentSerializer, SubjectSerializer, MarksSerializer, AttendanceSerializer, ExamSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().select_related('branch')
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
