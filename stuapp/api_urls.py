from rest_framework.routers import DefaultRouter

from .views import (
    StudentViewSet,
    StaffViewSet,
    BranchViewSet,
    AcadYearViewSet,
    SubjectViewSet,
    AttendanceViewSet,
    AttendanceReportViewSet,
    StudentLeaveViewSet,
    StaffLeaveViewSet,
    StudentFeedbackViewSet,
    StaffFeedbackViewSet,
    StudentNotificationViewSet,
    StaffNotificationViewSet,
)

router = DefaultRouter()

# Student
router.register(r'students', StudentViewSet, basename='students')

# Staff
router.register(r'staff', StaffViewSet, basename='staff')

# Branch
router.register(r'branches', BranchViewSet, basename='branches')

# Academic Year
router.register(r'academic-years', AcadYearViewSet, basename='academic-years')

# Subject
router.register(r'subjects', SubjectViewSet, basename='subjects')

# Attendance
router.register(r'attendance', AttendanceViewSet, basename='attendance')

# Attendance Report
router.register(r'attendance-reports', AttendanceReportViewSet, basename='attendance-reports')

# Student Leave
router.register(r'student-leaves', StudentLeaveViewSet, basename='student-leaves')

# Staff Leave
router.register(r'staff-leaves', StaffLeaveViewSet, basename='staff-leaves')

# Student Feedback
router.register(r'student-feedbacks', StudentFeedbackViewSet, basename='student-feedbacks')

# Staff Feedback
router.register(r'staff-feedbacks', StaffFeedbackViewSet, basename='staff-feedbacks')

# Student Notification
router.register(r'student-notifications', StudentNotificationViewSet, basename='student-notifications')

# Staff Notification
router.register(r'staff-notifications', StaffNotificationViewSet, basename='staff-notifications')

urlpatterns = router.urls