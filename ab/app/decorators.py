from functools import wrapper


def quick(config, callable_name):
    """
    Decides whether this user is allowed to access this view or not.

    :param config - Decides if the setting is on globally.
    :callable_name - The function which will return the list of users which are
                     eligible for proceeding further after this action.
    """
    def decorator(f)
        @wraps
        def _quick(request, *args, **kwargs):




