from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Employee
from .forms import EmployeeForm, SignUpForm


def index(request):
    employees = Employee.objects.all()
    if not employees:
        messages.info(request, "No employees found.")
    return render(request, 'index.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_employee.html', {
                'form': EmployeeForm(),
                'success': True
            })
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {
        'form': form
    })


def view_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    return render(request, "view_employee.html", {
        'employee': employee
    })

def edit_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, f"Employee {employee.first_name} {employee.last_name} updated successfully!")
            return redirect('index')
        else:
            messages.error(request, "There was an error updating the employee. Please try again.")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {
        'form': form,
        'employee': employee,
    })


def delete_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    
    if request.method == 'POST':
        employee.delete()
        messages.success(request, f"Employee {employee.first_name} {employee.last_name} has been deleted.")
        return redirect('index')
    
    return redirect('index')

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You're logged in!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful! You're now logged in.")
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
