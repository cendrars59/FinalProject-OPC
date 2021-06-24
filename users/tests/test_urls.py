from django.urls.base import resolve
import pytest
from django.urls import reverse
import config.urls

# testing pages urls for non connected user in order to ensure to retrieve the view associated with.
@pytest.mark.parametrize('param', [('login'), ('logout')])
def test_param_url_resolves_to_right_view(param):
    path = reverse(param)
    assert resolve(path).view_name == f'{param}'