from django.shortcuts import render
from django.views.generic.base import View

from .models import Employee


class EmployeeListView(View):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        return render(request, 'employees/employee_list.html', {'employees': employees})
