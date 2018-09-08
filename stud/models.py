from django.db import models

# Create your models here.
class student(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.IntegerField()

    def __str__(self):
        return str(self.name)