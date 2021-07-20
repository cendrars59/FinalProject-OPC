# see documentation for pytest.mark.urls
# https://pytest-django.readthedocs.io/en/latest/helpers.html#pytest.mark.urls
#from django.urls.base import resolve
import pytest
from django.urls import reverse, resolve
from practice import urls

#testing pages urls in order to ensure to retrieve the view associated with.
def test_param_url_resolves_to_new_view():
    path = reverse('practice-new')
    assert resolve(path).view_name == 'practice-new'


def test_param_url_resolves_to_list_view():
    path = reverse('practices-list')
    assert resolve(path).view_name == 'practices-list'


def test_param_url_resolves_to_detailed_view(practice1):
    path = reverse('practice-detail', kwargs={'pk':practice1.pk})
    assert resolve(path).view_name == 'practice-detail'

def test_param_url_resolves_to_update_view(practice1):
    path = reverse('practice-update', kwargs={'pk':practice1.pk})
    assert resolve(path).view_name == 'practice-update'
