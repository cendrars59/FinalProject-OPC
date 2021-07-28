# see documentation for pytest.mark.urls
# https://pytest-django.readthedocs.io/en/latest/helpers.html#pytest.mark.urls
#from django.urls.base import resolve
import pytest
from django.urls import reverse, resolve
from training_plan import urls

#testing pages urls in order to ensure to retrieve the view associated with.
def test_param_url_resolves_to_new_view():
    path = reverse('training_plan-new')
    assert resolve(path).view_name == 'training_plan-new'


def test_param_url_resolves_to_list_view():
    path = reverse('training_plan-list')
    assert resolve(path).view_name == 'training_plan-list'


def test_param_url_resolves_to_detailed_view(training_plan1):
    path = reverse('training_plan-detail', kwargs={'pk':training_plan1.pk})
    assert resolve(path).view_name == 'training_plan-detail'

def test_param_url_resolves_to_update_view(training_plan1):
    path = reverse('training_plan-update', kwargs={'pk':training_plan1.pk})
    assert resolve(path).view_name == 'training_plan-update'
