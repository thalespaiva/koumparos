from django.contrib import admin

# Register your models here.

from teacher.models import Teacher, Student, Class

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Class)
