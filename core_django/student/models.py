from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    age = models.IntegerField(default=18)
    std_class = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class StudentUser(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user_name