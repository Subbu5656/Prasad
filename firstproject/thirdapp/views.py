from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def Home(request):
	return render(request, 'thirdapp/home.html')

def HomeId(request, id):
	emp = Employee.objects.get(id=id)
	return render(request, 'thirdapp/home1.html', {'emp':emp})

def Add(request):
    if request.method =='POST':
        emp1 = Employee(
            name=request.POST.get('name'),
            company = request.POST.get('company'),
            location = request.POST.get('location'),
            salary = request.POST.get('salary'),
            gmail = request.POST.get('gmail'),
            mobile = request.POST.get('mobile'))
        emp1.save()
    return redirect('thirdapp/main/') 

def Main(request):
	emp = Employee.objects.all()
	return render(request, 'thirdapp/main.html', {'emp':emp})


def Del(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/thirdapp/main/')


def Update(request, id):
    if request.method=='POST':
        emp1 = Employee.objects.get(id=id)
        try:
            emp1.name=request.POST.get('name')
            emp1.company = request.POST.get('company')
            emp1.location = request.POST.get('location')
            emp1.salary = request.POST.get('salary')
            emp1.gmail = request.POST.get('gmail')
            emp1.mobile = request.POST.get('mobile')
            emp1.save()
        except Exception as E:
            print(E)
    return redirect('/thirdapp/main/')

















