from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def Home(request):
	return render(request, 'firstapp/home.html')

def HomeId(request, id):
	emp = Company.objects.get(id=id)
	return render(request, 'firstapp/home1.html', {'emp':emp})

def Main(request):
    emp = Company.objects.all()
    return render(request, 'firstapp/main.html', {'emp':emp})


def Add(request):
    if request.method =='POST':
        emp = Company(
            name=request.POST.get('name'),
            company = request.POST.get('company'),
            location = request.POST.get('location'),
            salary = request.POST.get('salary'),
            gmail = request.POST.get('gmail'),
            mobile = request.POST.get('mobile'))
        emp.save()
    return redirect('/firstapp/main/') 

def Del(request, id):
    emp = Company.objects.get(id=id)
    emp.delete()
    return redirect('/firstapp/main/')


def Update(request, id):
    if request.method=='POST':
        emp = Company.objects.get(id=id)
        try:
            emp.name=request.POST.get('name')
            emp.company = request.POST.get('company')
            emp.location = request.POST.get('location')
            emp.salary = request.POST.get('salary')
            emp.gmail = request.POST.get('gmail')
            emp.mobile = request.POST.get('mobile')
            emp.save()
        except Exception as E:
            print(E)
    return redirect('/firstapp/main/')

















