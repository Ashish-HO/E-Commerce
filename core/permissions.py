from rest_framework.permissions import BasePermission, SAFE_METHODS

# SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

#safe_method are accessed by anyone but post and delete method is done only by staff
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)

