# see documentation for pytest.mark.urls
# https://pytest-django.readthedocs.io/en/latest/helpers.html#pytest.mark.urls
#from django.urls.base import resolve
import pytest
from django.urls import reverse, resolve
from training_session import urls

#testing pages urls in order to ensure to retrieve the view associated with.
def test_param_url_resolves_to_new_view():
    path = reverse('training_session-new')
    assert resolve(path).view_name == 'training_session-new'


def test_param_url_resolves_to_list_view():
    path = reverse('training_session-list')
    assert resolve(path).view_name == 'training_session-list'


def test_param_url_resolves_to_detailed_view(training_session1):
    path = reverse('training_session-detail', kwargs={'pk':training_session1.pk})
    assert resolve(path).view_name == 'training_session-detail'

def test_param_url_resolves_to_update_view(training_session1):
    path = reverse('training_session-update', kwargs={'pk':training_session1.pk})
    assert resolve(path).view_name == 'training_session-update'
