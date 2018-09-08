from django.db import models

# Create your models here.
class Collage(models.Model):
    name=models.CharField(max_length=255, default="",null=True, blank=True)

    def __str__(self):
        return str(self.name)

class student(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.IntegerField()
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE, null=True,blank=True, default=1)

    def __str__(self):
        return str(self.name)