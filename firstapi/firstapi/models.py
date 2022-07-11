from django.db import models

class employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    emp_sal = models.IntegerField()
    email = models.CharField(max_length=40, default="123@gmail.com")

    def __str__(self) :
        return self.fname