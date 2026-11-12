from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Разрешает доступ к объекту только его создателю."""

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user