from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Employee
from .forms import EmployeeForm, SignUpForm


def index(request):
    return render(request, "index.html", {
        'employees': Employee.objects.all()
    })


def view_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    return render(request, "view_employee.html", {
        'employee': employee
    })


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


def edit_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return render(request, 'edit_employee.html', {
                'form': form,
                'success': True
            })
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {
        'form': form
    })


def delete_employee(request, id):
    if request.method == 'POST':
        employee = get_object_or_404(Employee, pk=id)
        employee.delete()
        return HttpResponseRedirect(reverse('index'))


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
