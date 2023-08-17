from django.views.generic import ListView
from django.shortcuts import render

from .models import Student
from .models import Teacher


def students_list(request):
    template = 'school/students_list.html'
    student = Student.objects.all().order_by('group')
    teacher = Teacher.objects.all()
    context = {'students':student, 'teachers': teacher}
    return render(request, template, context)
