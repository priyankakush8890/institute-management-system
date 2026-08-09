from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from .permissions import (
    IsHOD,
    IsStaff,
    IsStudent,
    IsHODOrStaff,
)
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

from .serializers import (
    StudentSerializer,
    StaffSerializer,
    BranchSerializer,
    AcadYearSerializer,
    SubjectSerializer,
    AttendanceSerializer,
    AttendanceReportSerializer,
    StudentLeaveSerializer,
    StaffLeaveSerializer,
    StudentFeedbackSerializer,
    StaffFeedbackSerializer,
    StudentNotificationSerializer,
    StaffNotificationSerializer,
)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()

    serializer_class = StudentSerializer

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated,IsHOD]

    filter_backends=[DjangoFilterBackend]

    filterset_fields=[
        "gender",
        "branch_id",
        "acad_year_id"
    ]

    filter_backends=[
    DjangoFilterBackend,
    SearchFilter
]

    search_fields=[
        "address",
        "studentmob"
    ]

    filter_backends=[
    DjangoFilterBackend,
    SearchFilter,
    OrderingFilter
]

    ordering_fields=[
        "created_at",
        "dob"
    ]

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsHOD]

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class AcadYearViewSet(viewsets.ModelViewSet):
    queryset = Acad_year.objects.all()
    serializer_class = AcadYearSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsHODOrStaff]
     

class AttendanceReportViewSet(viewsets.ModelViewSet):
    queryset = Attendance_report.objects.all()
    serializer_class = AttendanceReportSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StudentLeaveViewSet(viewsets.ModelViewSet):
    queryset = StudentLeave.objects.all()
    serializer_class = StudentLeaveSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StaffLeaveViewSet(viewsets.ModelViewSet):
    queryset = StaffLeave.objects.all()
    serializer_class = StaffLeaveSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StudentFeedbackViewSet(viewsets.ModelViewSet):
    queryset = StudentFeedback.objects.all()
    serializer_class = StudentFeedbackSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StaffFeedbackViewSet(viewsets.ModelViewSet):
    queryset = StaffFeedback.objects.all()
    serializer_class = StaffFeedbackSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StudentNotificationViewSet(viewsets.ModelViewSet):
    queryset = StudentNotification.objects.all()
    serializer_class = StudentNotificationSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StaffNotificationViewSet(viewsets.ModelViewSet):
    queryset = StaffNotifcation.objects.all()
    serializer_class = StaffNotificationSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
