

from rest_framework import serializers
from .models import (
    Student,
    Staff,
    Branch,
    Acad_year,
    Subject,
    Attendance,
    Attendance_report,
    StudentLeave,
    StaffLeave,
    StudentFeedback,
    StaffFeedback,
    StudentNotification,
    StaffNotifcation,
)


# Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


# Staff
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


# Branch
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


# Academic Year
class AcadYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acad_year
        fields = "__all__"


# Subject
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


# Attendance
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


# Attendance Report
class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance_report
        fields = "__all__"


# Student Leave
class StudentLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLeave
        fields = "__all__"


# Staff Leave
class StaffLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffLeave
        fields = "__all__"


# Student Feedback
class StudentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFeedback
        fields = "__all__"


# Staff Feedback
class StaffFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffFeedback
        fields = "__all__"


# Student Notification
class StudentNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentNotification
        fields = "__all__"


# Staff Notification
class StaffNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffNotifcation
        fields = "__all__"