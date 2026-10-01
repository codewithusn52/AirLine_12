from django import forms
from . models import ticketdetails  #for connecting models to form

class ticketForm(forms.Form):
    CLASS_CHOICES = [
        ('Economy class', 'Economy class'),
        ('Business class', 'Business class'),
        ('Upper high class', 'Upper high class'),
        ('High class', 'High class'),
        ('Middle class', 'Middle class'),
    ]
    name=forms.CharField(max_length=100)
    m_no=forms.CharField(max_length=10)
    age=forms.CharField()
    add=forms.CharField(max_length=200)
    dest=forms.CharField(max_length=50)
    Bank_name = forms.CharField(max_length=100)
    accNo = forms.CharField(max_length=50)
    code = forms.CharField(max_length=20)
    travel_class = forms.ChoiceField(choices=CLASS_CHOICES)
    time = forms.TimeField(label='Enter your preferred Time')


