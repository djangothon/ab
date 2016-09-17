from django import template
from ..utils import function_from_string

register = template.Library()


class InExperiment(template.Node):
    def __init__(self, *args, **kwargs):
        self.config = kwargs['config']
        self.callable_name = kwargs['callable_name']
        self.only_authenticated = kwargs.get('only_authenticated', True)

    def render(self, context):
        # Check if the config is available globally and return '' or raise
        # 404 as per the nature of the request.
        if not self.config:
            return False

        request = template.Variable('request').resolve(context)
        user = request.user

        # The user will not be shown the feature if and only if
        # authentication is required and the user is not authenticated.
        if self.only_authenticated and not user.is_authenticated():
            return False

        # Get the function object which needs to called in order to get the
        # control group for the experiment
        _callable = function_from_string(self.callable_name)
        if user.id in _callable():
            return True

        return False


@register.tag
def ifinexperiment(parser, token):
    bits = token.split_contents()[1:]
    lbits = len(bits)
    kwargs = {}

    if lbits <= 3:
        kwargs = {
            'config': bits[1],
            'callable_name': bits[2]
        }
    if lbits == 3:
        kwargs.update({'only_authenticated': bits[-1]})

    return InExperiment(**kwargs)
