from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.db.models import Q




# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    emp_data = {
        'emp_details': emps
    }
    print(emp_data)
    return render(request, 'view_all_emp.html', emp_data)


def add_emp(request):

    departments = Department.objects.all()
    roles = Role.objects.all()

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hire_date=datetime.now() )
        new_emp.save()
        return HttpResponse("Employee is added successfully")

    
    elif request.method == "GET": 
     context = {
             'departments': departments,
             'roles': roles}
     
     return render(request, 'add_emp.html', context)

    else:
        return HttpResponse("There is an error, Employee not added successfully. Please try again !!!")


def remove_emp(request, emp_id = 0):
     if emp_id:
         try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee is removed successfully')
         except:
             return HttpResponse("Please enter a valid emp id")    
     emps = Employee.objects.all()
     emp_data = {
         'emp_details' : emps
     }
     print(emp_data)
     return render(request, 'remove_emp.html', emp_data )


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name :
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept :
            emps = emps.filter(dept__name__icontains = dept)
        if role :
            emps = emps.filter(role__name__icontains = role)

        emp_data = {
            'emp_details' : emps
        }
        return render(request, 'view_all_emp.html', emp_data)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')

    else:
        return HttpResponse('Employee not found')
    
