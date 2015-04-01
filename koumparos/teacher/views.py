# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

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
        'students': Student.objects.all(),
    }

    if request.method == "POST":
        student = Student.objects.filter(id=request.POST['student_id'])[0]
        teacher = info['teacher']
        price = request.POST['price']
        date = request.POST['class_date']
        start = request.POST['start_time']
        finish = request.POST['finish_time']
        location = request.POST['location']

        new_class = Class(
            student=student, teacher=teacher, subject='MATH',
            price=price, location=location, date=date, start_time=start,
            finish_time=finish)
        new_class.save()

    return render_to_response('teacher/schedule.html', info,
                              RequestContext(request))
