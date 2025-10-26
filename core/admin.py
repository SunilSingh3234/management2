from django.contrib import admin
from .models import Branch, Student, Subject, Marks, Attendance, Exam

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name','code')
    search_fields = ('name','code')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('enrollment_no','first_name','last_name','branch','year','user')
    search_fields = ('enrollment_no','first_name','last_name')
    list_filter = ('branch','year')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name','code','branch','semester')
    list_filter = ('branch','semester')

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('student','subject','marks_obtained','max_marks')
    search_fields = ('student__enrollment_no','student__first_name')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student','date','present')
    list_filter = ('date','present')

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name','date')
