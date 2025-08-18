from django.shortcuts import render, redirect, get_object_or_404
from .teacherForm import TeacherRegisterForm
from .models import Teacher

def teacher_register(request):
    if request.method == "POST":
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("teacher_success")  # define success page
    else:
        form = TeacherRegisterForm()
    return render(request, "teacher_register.html", {"form": form})

def teacher_success(request):
    return render(request, 'teacher_success.html')

def teacher_detail(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})