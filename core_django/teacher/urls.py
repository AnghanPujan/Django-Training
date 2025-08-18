from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.teacher_register, name="teacher_register"),
    path("teacher_success/", views.teacher_success, name="teacher_register"),
    path('teacher/<int:id>/', views.teacher_detail, name='teacher_detail'),
]
    