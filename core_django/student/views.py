from django.shortcuts import render, redirect
from student.models import student, StudentUser
from .StudentRegisterForm import StudentRegisterForm  # Use a clear class name
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Show all students
def all(request):
    students = student.objects.all()
    return render(request, 'student/all.html', {'students': students})

# Show single student (example with name filter)
def single(request):
    selected_student = student.objects.get(name='og')
    return render(request, 'student/single.html', {'student': selected_student})

def register(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        pass
        if form.is_valid():
            StudentUser.objects.create(
                user_name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
    else:
        form = StudentRegisterForm()
    return render(request, 'student/register.html', {'form': form})
