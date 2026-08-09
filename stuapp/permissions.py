from rest_framework.permissions import BasePermission

class IsHOD(BasePermission):
    """
    Only HOD can access.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.user_type == "1"
        )

class IsStaff(BasePermission):
    """
    Only Staff can access.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.user_type == "2"
        )

class IsStudent(BasePermission):
    """
    Only Students can access.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.user_type == "3"
        )

from rest_framework.permissions import BasePermission

class IsHODOrStaff(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated and
            request.user.user_type in ["1", "2"]
        )