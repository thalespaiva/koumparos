# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
# from django.http import HttpResponse

from datetime import datetime, timedelta

from teacher.models import Teacher, Student, Class

# Create your views here.


def overview(request, id):

    if request.method == "POST":
        updated_class = request.POST['updated_class']
        tgt_status = request.POST['class_status_' + updated_class]
        tgt_class = Class.objects.filter(id=updated_class)[0]

        tgt_class.status = tgt_status
        tgt_class.save()

    max_date = (datetime.now() + timedelta(days=14)).date
    todo_classes = Class.objects.filter(teacher=id, status=Class.ST_TODO, date__lte=max_date)
    info = {
        'teacher': Teacher.objects.filter(id=id)[0],
        'classes': todo_classes.order_by('date', 'start_time'),
        'status_choices': Class.STATUS_CHOICES,
    }
    return render_to_response('teacher/overview.html', info,
                              RequestContext(request))


def schedule(request, id):
    info = {
        'teacher': Teacher.objects.filter(id=id)[0],
        'students': Student.objects.all(),
    }

    if request.method == "POST":
        student = Student.objects.filter(id=request.POST['student_id'])[0]
        teacher = info['teacher']
        price = request.POST['price']
        base_date = request.POST['class_date']
        start = request.POST['start_time']
        finish = request.POST['finish_time']
        location = request.POST['location']

        number_of_weeks = request.POST['number_of_weeks']
        date = datetime.strptime(base_date, '%Y-%m-%d')
        for i in range(int(number_of_weeks)):
            new_class = Class(
                student=student, teacher=teacher, subject='MATH',
                price=price, location=location, date=date.date(),
                start_time=start, finish_time=finish)
            new_class.save()
            date = date + timedelta(days=7)

    return render_to_response('teacher/schedule.html', info,
                              RequestContext(request))


def dashboard(request, id):
    from django.db.models import Sum

    classes_this_month = Class.objects.filter(
        teacher_id=id, date__month=datetime.now().month)
    expected_earnings_this_month = classes_this_month.aggregate(Sum("price"))

    info = {
        'teacher': Teacher.objects.filter(id=id)[0],
        'month_target': expected_earnings_this_month,
    }

    return render_to_response('teacher/dashboard.html', info)
