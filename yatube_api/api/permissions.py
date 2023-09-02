from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    """
    Кастомное разрешение на редактирование,
    удаление определенного объекта
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
