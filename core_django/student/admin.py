from django.contrib import admin
from student.models import student 

# admin.site.register(student)

@admin.register(student)   # Regestration of the tabel in admin panel
class StudentAdmin(admin.ModelAdmin): # setting the view of the tabel in admin panel 
    list_display = ('name', 'age', 'roll_no') # parameters which will shown to admin