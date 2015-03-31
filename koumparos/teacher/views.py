from django.shortcuts import render
from django.shortcuts import render_to_response

from teacher.models import Class

# Create your views here.
def home(request):
    return render_to_response('teacher/overview.html', {'classes' : Class.objects.all()})
