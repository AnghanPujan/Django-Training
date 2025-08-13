from django.shortcuts import render, redirect
from student.models import student, StudentUser
from .StudentRegisterForm import StudentRegisterForm, StudentLoginForm  # Use a clear class name
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
        if form.is_valid():
            user_name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['cpassword']

            if password != cpassword:
                messages.error(request, "Passwords do not match.")
                return redirect('register')

            if StudentUser.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
                return redirect('register')

            # Save new user (for production: use make_password(password))
            StudentUser.objects.create(
                user_name=user_name,
                email=email,
                password=password
            )
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = StudentRegisterForm()

    return render(request, 'student/register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = StudentUser.objects.get(email=email)
            except StudentUser.DoesNotExist:
                messages.error(request, "No account found with that email.")
                return redirect('login')

            # For production: use check_password(password, user.password)
            if user.password == password:
                messages.success(request, "Login successful!")
                return redirect('home')
            else:
                messages.error(request, "Invalid password.")
                return redirect('login')
    else:
        form = StudentLoginForm()

    return render(request, 'student/login.html', {'form': form})


def home(request):
    return render(request, 'student/home.html')

