from django.test import RequestFactory
import pytest
from django import urls
from django.contrib.auth import get_user_model
from users.models import CustomUser
from pytest_django.asserts import assertTemplateUsed
from pages.views import legal, information, home
from django.urls.base import resolve

# testing routing for each url to the correct views
# belonging to the pages app
# 200 is expected response from GET request
# and verify also that the right template is returned
# Here we are testing the urls in the list passed as param
@pytest.mark.django_db
def test_render_practices_list_view(client, user1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.force_login(user1)
    path = urls.reverse('practices-list')
    response = client.get(path)
    assert response.status_code == 200

def test_should_use_correct_template_to_render_list_view(client,user1):
    client.force_login(user1)
    path = urls.reverse('practices-list')
    response = client.get(path)
    assertTemplateUsed(response, 'practice/practice_list.html')
    

@pytest.mark.django_db
def test_render_practice_new_view(client, user1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.force_login(user1)
    path=urls.reverse('practice-new')
    response = client.get(path)
    assert response.status_code == 200

def test_should_use_correct_template_to_render_new_view(client,user1):
    client.force_login(user1)
    path = urls.reverse('practice-new')
    response = client.get(path)
    assertTemplateUsed(response, 'practice/practice_form.html')
    

@pytest.mark.django_db
def test_render_practice_detailed_view(client, user1, practice1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.force_login(user1)
    path = urls.reverse('practice-detail', kwargs={'pk':practice1.pk})
    response = client.get(path)
    assert response.status_code == 200

# def test_should_use_correct_template_to_render_detailed_view(client, practice1, user1):
#     client.force_login(user1)
#     response = client.get(f'practices/{practice1.id}')
#     assertTemplateUsed(response, 'practice/practice_detail.html')


@pytest.mark.django_db
def test_render_practice_update_view(client, user1, practice1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.force_login(user1)
    path = urls.reverse('practice-update', kwargs={'pk':practice1.pk})
    response = client.get(path)
    assert response.status_code == 200
    