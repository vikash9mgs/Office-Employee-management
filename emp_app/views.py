from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department,adminInfo
from datetime import datetime
from django.db.models import Q


# Create your views here.

def index(request):
    try:
        context = {
            'chkadmin': request.session['email']
        }
        if request.session['email'] == None:
            return render(request, 'index.html',context)
        else:
            return render(request, 'index.html',context)
    except:
        return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')


def all_emp(request):
    try:

        if request.session['email'] == None:
            return render(request, 'index.html')
        emps = Employee.objects.all()
        context = {
            'emps': emps
        }

        return render(request, 'view_all_emp.html', context)
    except:
        return index(request)

def add_emp(request):
    try:
        if not request.session['email']:
            return render(request, 'index.html')
    except:
        return index(request)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        address = request.POST['address']
        email = request.POST['email']
        dept = request.POST['dept']
        role = request.POST['role']
        location = request.POST['location']
        # photo = request.POST['photo']
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone,
                           address=address, email=email, location=location,
                           dept=dept, role=role, hire_date=datetime.now())
        new_emp.save()
        return render(request, 'add_emp.html', {'msg': 'Employee added Successfully'})
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occurred! Employee Has Not Been Added")


def remove_emp(request, emp_id=0):
    try:
        if not request.session['email']:
            return render(request, 'index.html')
    except:
        return index(request)
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid Emp Id")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    try:
        if not request.session['email']:
            return render(request, 'index.html')
    except:
        return index(request)
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__icontains=dept)
        if role:
            emps = emps.filter(role__icontains=role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')


def profile(request, id):
    emp_Profile = Employee.objects.get(id=id)
    context = {'emp': emp_Profile}
    return render(request, 'profile.html', context)


def edit_profile(request):
    if not request.session['email']:
        return render(request, 'index.html')
    id = request.POST['id']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    phone = int(request.POST['phone'])
    address = request.POST['address']
    email = request.POST['email']
    role = request.POST['role']
    department = request.POST['department']
    hire_date = datetime.now()
    bonus = request.POST['bonus']
    salary = request.POST['salary']
    location = request.POST['location']
    # photo = request.POST['photo']
    try:
        Employee.objects.filter(id=id).update(first_name=first_name, last_name=last_name, phone=phone, address=address,
                                              role=role, email=email, dept=department, hire_date=hire_date,
                                              bonus=bonus, salary=salary, location=location)
    except Exception as e:
        return HttpResponse(e)
    return HttpResponseRedirect(f"http://127.0.0.1:8000/profile/{id}")
    return render(request, 'profile.html')


def login(request):
    try:
        id = request.POST['id']
        password = request.POST['password']
        try:
            admin = adminInfo.objects.get(email=id, psd=password)
        except:
            return render("Email Not Matched")
        request.session['email'] = id
        context = {
            'chkadmin': request.session['email']
        }
    except:
        context = {
            'chkadmin': request.session['email']
        }
        return HttpResponse('Wrong Email or Password')
    return render(request, 'index.html',context)

    # return render(request, 'index.html',context)

def logout(request):
    request.session['email'] = None
    return render(request, 'index.html')