from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employee(MPTTModel):
    fio = models.CharField(max_length=255, verbose_name='ФИО сотрудника')
    salary = models.PositiveIntegerField(verbose_name='Зарплата')
    position = models.CharField(max_length=150, verbose_name='Должность')
    onboarding_date = models.DateField(auto_now_add=False)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='reporters')

    class MPTTMeta:
        order_insertion_by = ['fio']

    def __str__(self):
        return f'{self.fio} - {self.position} | Salary - {self.salary}р. | Onboarding date - {self.onboarding_date} |'

