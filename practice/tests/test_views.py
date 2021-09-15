from django.test import RequestFactory
import pytest
from django import urls
from django.contrib.auth import get_user_model
from users.models import CustomUser
from pytest_django.asserts import assertTemplateUsed
from pages.views import legal, information, home
from django.urls.base import resolve
import time

# testing routing for each url to the correct views
# belonging to the pages app
# 200 is expected response from GET request
# and verify also that the right template is returned
# Here we are testing the urls in the list passed as param


@pytest.mark.django_db
def test_render_practices_list_view(client, user1, user1_involved_in_season1_as_manager):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.login(username=user1.email, password="totor")
    path = urls.reverse('practices-list')
    response = client.get(path, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_use_correct_template_to_render_list_view(client, user1, user1_involved_in_season1_as_manager):
    client.get('login/')
    client.login(username=user1.email, password="totor")
    path = urls.reverse('practices-list')
    response = client.get(path, follow=True)
    assertTemplateUsed(response, 'practice/practice_list.html')


@pytest.mark.django_db
def test_render_practice_new_view(client, user1, user1_involved_in_season1_as_manager):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.get('login/')
    client.login(username=user1.email, password="totor")
    path = urls.reverse('practice-new')
    response = client.get(path, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_use_correct_template_to_render_new_view(client, user1, user1_involved_in_season1_as_manager):
    client.login(username=user1.email, password="totor")
    path = urls.reverse('practice-new')
    response = client.get(path, follow=True)
    assertTemplateUsed(response, 'practice/practice_form.html')


@pytest.mark.django_db
def test_render_practice_detailed_view(client, user1, user1_involved_in_season1_as_manager, practice1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.get('login/')
    client.login(username=user1.email, password="totor")
    path = urls.reverse('practice-detail', kwargs={'pk': practice1.pk})
    response = client.get(path, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_use_correct_template_to_render_detailed_view(client, practice1, user1, user1_involved_in_season1_as_manager):
    client.get('login/')
    client.login(username=user1.email, password="totor")
    path = urls.reverse('practice-detail', kwargs={'pk': practice1.pk})
    response = client.get(path, follow=True)
    assertTemplateUsed(response, 'practice/practice_detail.html')


@pytest.mark.django_db
def test_render_practice_update_view(client, user1, user1_involved_in_season1_as_manager, practice1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.get('login/')
    client.login(username=user1.email, password="totor")
    path = urls.reverse('practice-update', kwargs={'pk': practice1.pk})
    response = client.get(path, follow=True)
    assert response.status_code == 200
