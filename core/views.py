from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Branch
from django.db.models import Q

class StudentListView(ListView):
    model = Student
    paginate_by = 10
    template_name = 'core/student_list.html'
    def get_queryset(self):
        q = self.request.GET.get('q','')
        qs = super().get_queryset().select_related('branch')
        if q:
            qs = qs.filter(Q(first_name__icontains=q)|Q(last_name__icontains=q)|Q(enrollment_no__icontains=q)|Q(branch__name__icontains=q))
        branch = self.request.GET.get('branch')
        if branch:
            qs = qs.filter(branch__id=branch)
        return qs.order_by('enrollment_no')

class StudentDetailView(DetailView):
    model = Student
    template_name = 'core/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['enrollment_no','first_name','last_name','email','phone','photo','dob','branch','year','address']
    template_name = 'core/student_form.html'
    success_url = reverse_lazy('students:list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['enrollment_no','first_name','last_name','email','phone','photo','dob','branch','year','address']
    template_name = 'core/student_form.html'
    success_url = reverse_lazy('students:list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'core/student_confirm_delete.html'
    success_url = reverse_lazy('students:list')

# student auth views
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentLoginForm
from django.contrib import messages
from django.urls import reverse

def student_login(request):
    if request.user.is_authenticated:
        return redirect('student_dashboard')
    if request.method == 'POST':
        form = StudentLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = StudentLoginForm()
    return render(request, 'core/student_login.html', {'form': form})

@login_required
def student_dashboard(request):
    try:
        student = request.user.student
    except Exception:
        messages.error(request, 'No student profile linked to your account.')
        return redirect(reverse('students:list'))
    marks = student.marks.select_related('subject').all()
    attendance = student.attendance.all().order_by('-date')[:50]
    return render(request, 'core/student_dashboard.html', {'student': student, 'marks': marks, 'attendance': attendance})

@login_required
def student_logout(request):
    logout(request)
    return redirect('student_login')
