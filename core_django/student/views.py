from django.shortcuts import render
from student.models import student

# Show all students
def all(request):
    students = student.objects.all()
    return render(request, 'student/all.html', {'students': students})

# Show single student (example with name filter)
def single(request):
    selected_student = student.objects.get(name='og')
    return render(request, 'student/single.html', {'student': selected_student})
