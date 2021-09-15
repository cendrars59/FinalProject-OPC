from django.test import RequestFactory
import pytest
from django.urls import reverse
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
def test_render_training_session_list_view(client, user1, user1_involved_in_season1_as_manager):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.login(username=user1.email, password="totor")
    path = reverse('training_session-list')
    response = client.get(path)
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_use_correct_template_to_render_list_view(client, user1, user1_involved_in_season1_as_manager):
    client.login(username=user1.email, password="totor")
    response = client.get(reverse('training_session-list'), follow=True)
    #assert response.templates == 'training_session/trainingsession_list.html'
    assertTemplateUsed(response, 'training_session/trainingsession_list.html')


@pytest.mark.django_db
def test_render_practice_new_view(client, user1, user1_involved_in_season1_as_manager):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.login(username=user1.email, password="totor")
    path = reverse('training_session-new')
    response = client.get(path, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_use_correct_template_to_render_new_view(client, user1, user1_involved_in_season1_as_manager):
    client.login(username=user1.email, password="totor")
    path = reverse('training_session-new')
    response = client.get(path, follow=True)
    assertTemplateUsed(response, 'training_session/trainingsession_form.html')


@pytest.mark.django_db
def test_render_training_session_detailed_view(client, user1, user1_involved_in_season1_as_manager, training_session1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.login(username=user1.email, password="totor")
    path = reverse('training_session-detail', kwargs={'pk': training_session1.pk})
    response = client.get(path)
    assert response.status_code == 200

# def test_should_use_correct_template_to_render_detailed_view(client, training_session1, user1):
#     client.force_login(user1)
#     response = client.get(f'training_sessions/{training_session1.id}')
#     assertTemplateUsed(response, 'training_session/trainingsession_detail.html')


@pytest.mark.django_db
def test_render_training_session_update_view(client, user1, user1_involved_in_season1_as_manager, training_session1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.login(username=user1.email, password="totor")
    path = reverse('training_session-update', kwargs={'pk': training_session1.pk})
    response = client.get(path)
    assert response.status_code == 200
