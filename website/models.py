from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}"
