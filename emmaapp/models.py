from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    matric_number = models.CharField(max_length=50, unique=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    resume = models.FileField(upload_to='resumes/')
    result = models.FileField(upload_to='results/')
    essay1 = models.FileField(upload_to='essays/')
    essay2 = models.FileField(upload_to='essays/')
    essay3 = models.FileField(upload_to='essays/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
