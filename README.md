django-ab
=========

AB-Testing framework with a difference.

An easily pluggable utility for doing control group testing of components
in django web applications.

The application focuses importance of testing the product on actual users
before going for the final release.

Usage
=====

- Install the package
`pip install django-ab`

- Add feature flag to distinguish a particular feature. Note that the flag
  should start with `F`. The feature flag control the behaviour to turn on/off
  the feature for the users.

  For example, if you have a feature flag `F_SHOW_ADS` set to `True` it would
  turn on the ads for the set of users and `False` would turn off that feature.

- Using it as a decorator?
`@quick(<feature_flag>, <callable_name>, only_authenticated=[True|False])`

Here `callable name` is the name of the experiment that you want to conduct on
the set of users.

- Using it as a django templatetag?
`{% ifexperiment feature_flag callable_name only_authenticated=[True|False] %}
    <!-- Logic goes here -->
 {% elifexperiment ... %}
    ...
 {% endif %}
`

Future Scope
============

- Add support for multiple experimets on the same view in the view layer itself.
- Build analytics tool to give the developers a better idea on which strategies
  turns out to be better
- PEP8 fixes and rolling out django-ab.readthedocs.org
