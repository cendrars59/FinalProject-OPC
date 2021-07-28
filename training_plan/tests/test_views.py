from django.test import RequestFactory
import pytest
from django import urls
from django.contrib.auth import get_user_model
from users.models import CustomUser
from pytest_django.asserts import assertTemplateUsed
#from training_plan.views import legal, information, home
from django.urls.base import resolve

# testing routing for each url to the correct views
# belonging to the pages app
# 200 is expected response from GET request
# and verify also that the right template is returned
# Here we are testing the urls in the list passed as param
@pytest.mark.django_db
def test_render_training_plan_list_view(client, user1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.force_login(user1)
    path = urls.reverse('training_plan-list')
    response = client.get(path)
    assert response.status_code == 200

def test_should_use_correct_template_to_render_list_view(client,user1):
    client.force_login(user1)
    path = urls.reverse('training_plan-list')
    response = client.get(path)
    assertTemplateUsed(response, 'training_plan/trainingplan_list.html')
    

@pytest.mark.django_db
def test_render_practice_new_view(client, user1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.force_login(user1)
    path=urls.reverse('training_plan-new')
    response = client.get(path)
    assert response.status_code == 200

def test_should_use_correct_template_to_render_new_view(client,user1):
    client.force_login(user1)
    path = urls.reverse('training_plan-new')
    response = client.get(path)
    assertTemplateUsed(response, 'training_plan/trainingplan_form.html')
    

@pytest.mark.django_db
def test_render_training_plan_detailed_view(client, user1, training_plan1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.force_login(user1)
    path = urls.reverse('training_plan-detail', kwargs={'pk':training_plan1.pk})
    response = client.get(path)
    assert response.status_code == 200

# def test_should_use_correct_template_to_render_detailed_view(client, training_plan1, user1):
#     client.force_login(user1)
#     path = urls.reverse('training_plan-detail')
#     response = client.get(path)
#     assertTemplateUsed(response, 'training_plan/trainingplan_detail.html')


@pytest.mark.django_db
def test_render_training_plan_update_view(client, user1, training_plan1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.force_login(user1)
    path = urls.reverse('training_plan-update', kwargs={'pk':training_plan1.pk})
    response = client.get(path)
    assert response.status_code == 200
    