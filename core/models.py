from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Branch(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    def __str__(self): return f"{self.name} ({self.code})"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    enrollment_no = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, related_name='students')
    year = models.PositiveSmallIntegerField(default=1)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return f"{self.enrollment_no} - {self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='subjects')
    semester = models.PositiveSmallIntegerField(default=1)
    def __str__(self): return f"{self.name} ({self.code})"

class Exam(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    description = models.TextField(blank=True)
    def __str__(self): return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True, blank=True)
    exam_date = models.DateField(null=True, blank=True)
    @property
    def percentage(self):
        try:
            return (self.marks_obtained / self.max_marks) * 100
        except:
            return 0
    @property
    def grade(self):
        p = self.percentage
        if p>=85: return 'A'
        if p>=70: return 'B'
        if p>=50: return 'C'
        if p>=35: return 'D'
        return 'F'

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    present = models.BooleanField(default=True)
    remarks = models.TextField(blank=True)
    class Meta:
        unique_together = ('student','date')
