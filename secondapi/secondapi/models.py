from django.db import models

class employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    emp_sal = models.IntegerField(default=20000)
    email = models.CharField(max_length=40, default="123@gmail.com")

    def __str__(self) :
        return self.fname

class department(models.Model):
    dept_name = models.CharField(max_length=20)
    dept_id = models.IntegerField()
    dept_budget  = models.IntegerField()
    dept_employees = models.IntegerField()

    def __str__(self) :
        return self.dept_name

    