from functools import wraps
from django.http import Http404
from django.http import HttpResponse

from .utils import function_from_string


def quick(config, callable_name, only_authenticated=True):
    """
    Decides whether this user is allowed to access this view or not.

    :param config - Decides if the setting is on globally.
    :callable_name - The function which will return the list of users which are
                     eligible for proceeding further after this action.
    """

    def _return_blank_or_raise_404(is_ajax):
        """
        Return empty string '' in case of ajax requests and raise 404 in case
        of non-ajax requests.
        """
        if is_ajax:
            return HttpResponse('')
        else:
            raise Http404

    def decorator(func):
        @wraps
        def _quick(request, *args, **kwargs):

            # Check if the request is ajax.
            is_ajax = request.is_ajax()

            # Check if the config is available globally and return '' or raise
            # 404 as per the nature of the request.
            if not config:
                _return_blank_or_raise_404(is_ajax)

            user = request.user

            # The user will not be shown the feature if and only if
            # authentication is required and the user is not authenticated.
            if only_authenticated and not user.is_authenticated():
                _return_blank_or_raise_404(is_ajax)

            # Get the function object which needs to called in order to get the
            # control group for the experiment
            _callable = function_from_string(callable_name)
            if user.id in _callable():
                return func(request, *args, **kwargs)
            else:
                _return_blank_or_raise_404(is_ajax)
