from rest_framework import permissions


class DefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        model_name = self.__get_model_name(request.method, view)
        return False

    def __get_model_name(self, method, view):
        try:
            model_name = view.get_queryset().model.__name__
            app_label = view.get_queryset().model._meta.app_label
            action = self.__get_method_action(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None

    def __get_method_action(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
