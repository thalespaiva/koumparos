# from django.shortcuts import render
from django.shortcuts import render_to_response

from teacher.models import Teacher, Student, Class

# Create your views here.


def overview(request, id):
    info = {
        'teacher': Teacher.objects.filter(id=id)[0],
        'classes': Class.objects.filter(teacher=id),
    }
    return render_to_response('teacher/overview.html', info)


def schedule(request, id):
    info = {
        'teacher': Teacher.objects.filter(id=id)[0],
        'classes': Class.objects.filter(teacher=id),
        'students': Student.objects.all(),
    }
    return render_to_response('teacher/schedule.html', info)
