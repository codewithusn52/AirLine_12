from django.db import models

# Create your models here.
class ticketdetails(models.Model):
    CLASS_CHOICES = [
        ('Economy class', 'Economy class'),
        ('Business class', 'Business class'),
        ('Upper high class', 'Upper high class'),
        ('High class', 'High class'),
        ('Middle class', 'Middle class'),
    ]
    name=models.CharField(max_length=100)
    m_no=models.CharField(max_length=10)
    age=models.PositiveIntegerField()
    add=models.CharField(max_length=200)
    dest=models.CharField(max_length=50)
    Bank_name = models.CharField(max_length=100)
    accNo = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    travel_class = models.CharField(choices=CLASS_CHOICES)
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.dest}"