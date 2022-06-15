from django.shortcuts import render
from django.views.generic import ListView
from .models import Employees
# Create your views here.


class ListEmployeesView(ListView):
    model = Employees
    queryset = Employees.objects.all().order_by('name')


