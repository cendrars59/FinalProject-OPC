# see documentation for pytest.mark.urls
# https://pytest-django.readthedocs.io/en/latest/helpers.html#pytest.mark.urls
from django.urls.base import resolve
import pytest
from django.urls import reverse
from pages import urls

# testing pages urls in order to ensure to retrieve the view associated with.
@pytest.mark.parametrize('param', [('home'), ('information'), ('legal')])
def test_param_url_resolves_to_right_view(param):
    path = reverse(param)
    assert resolve(path).view_name == f'{param}'
