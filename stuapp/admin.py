from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin
# Register your models here.
# admin.site.register(CustomUser)


class UserModel(UserAdmin):
    list_display=['username','user_type']
    
admin.site.register(CustomUser,UserModel)

admin.site.register(Acad_year)
admin.site.register(Branch)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(StudentLeave)
admin.site.register(StaffLeave)
admin.site.register(StudentNotification)
admin.site.register(StaffNotifcation)
admin.site.register(StudentFeedback)
admin.site.register(StaffFeedback)
admin.site.register(Attendance)
admin.site.register(Attendance_report)