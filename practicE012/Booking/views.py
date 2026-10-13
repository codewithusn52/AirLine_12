from django.shortcuts import redirect, render
from . import forms
from . import models
def bookticket(request):
    if request.method == 'POST':
        f=forms.ticketForm(request.POST)
        if f.is_valid():
            models.ticketdetails.objects.create(
                name = f.cleaned_data['name'],
                m_no = f.cleaned_data['m_no'],
                age = f.cleaned_data['age'],
                add = f.cleaned_data['add'],
                dest = f.cleaned_data['dest'],
                Bank_name=f.cleaned_data['Bank_name'],
                accNo=f.cleaned_data['accNo'],
                code=f.cleaned_data['code'],
                travel_class = f.cleaned_data['travel_class'],
                time = f.cleaned_data['time']
                )     
    else:
        f=forms.ticketForm()   
    return render(request,'bookticket.html',{'form':f})

def viewTicket(request, id):
    rec=models.ticketdetails.objects.get(id=id)
    if request.method == 'POST':
        f=forms.ticketForm(request.POST)
        if f.is_valid():
            for field, value in f.cleaned_data.items():
                setattr(rec, field, value)
            rec.save()
            return redirect('viewT', id=rec.id)
    else:
        f=forms.ticketForm(initial={
            field: getattr(rec, field)
            for field in (
                'name', 'm_no', 'age', 'add', 'dest', 'Bank_name',
                'accNo', 'code', 'travel_class', 'time',
            )
        })
    return render(request,'bookticket.html',{'form':f})
    '''name=request.GET['name']
    mobile_number=request.GET['m_no']
    Age=request.GET['age']
    Address=request.GET['add']
    Destination=request.GET['dest']
    Bank_name=request.GET['Bank_name']
    Account_No=request.GET['accNo']
    IFSC_CODE=request.GET['code']
    travel_Class=request.GET['travel_class']
    Time = request.GET['time']
    air_dict={
        'name': name, 'mobile_number':mobile_number, 'age': Age, 'Add':Address, 'dest':Destination,
        'BName': Bank_name,'AcNo': Account_No, 'IFSC': IFSC_CODE,'TravelC':travel_Class,'time': Time,
        }
    return render (request,'e_ticket.html',air_dict)
'''
