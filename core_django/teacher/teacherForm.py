from django import forms
from .models import Teacher

class TeacherRegisterForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email', 'subject', 'salary'] 