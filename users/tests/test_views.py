import pytest
from django.urls import reverse
from django.test import RequestFactory
from django import urls
from django.contrib.auth import get_user_model
from users.models import CustomUser
from pytest_django.asserts import assertTemplateUsed
# from training_plan.views import legal, information, home
from django.urls.base import resolve


@pytest.mark.django_db
def test_with_authenticated_client(client, user1, user1_involved_in_season1_as_manager):
    client.login(username=user1.email, password="totor")
    path = reverse('home')
    response = client.get(path, follow=True)
    content = response.content.decode(response.charset)
    # Verify that the user is connected and his or her first name is displayed on the page
    assert response.status_code == 200
    assert '<a id="url-legal" class="text-muted" href="/legal">Legal</a>' in content
    assert 'href="https://www.rugby-tourcoing.com/"' in content


@pytest.mark.django_db
def test_render_players_list_view(client, user1, user1_involved_in_season1_as_manager, category1, season1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.login(username=user1.email, password="totor")
    path = urls.reverse('players_list', kwargs={'category_id': category1.pk, 'season_id': season1.pk})
    response = client.get(path, follow=True)
    assert response.status_code == 200


@ pytest.mark.django_db
def test_should_use_correct_template_to_render_playerlist_view(client, user1, user1_involved_in_season1_as_manager, category1, season1):
    client.login(username=user1.email, password="totor")
    path = urls.reverse('players_list', kwargs={'category_id': category1.pk, 'season_id': season1.pk})
    response = client.get(path, follow=True)
    assertTemplateUsed(response, 'users/PlayersListCatSeason.html')


@pytest.mark.django_db
def test_render_managers_list_view(client, user1, user1_involved_in_season1_as_manager, category1, season1):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.login(username=user1.email, password="totor")
    path = urls.reverse('managers_list', kwargs={'category_id': category1.pk, 'season_id': season1.pk})
    response = client.get(path, follow=True)
    assert response.status_code == 200


@ pytest.mark.django_db
def test_should_use_correct_template_to_render_managerlist_view(client, user1, user1_involved_in_season1_as_manager, category1, season1):
    client.login(username=user1.email, password="totor")
    path = urls.reverse('managers_list', kwargs={'category_id': category1.pk, 'season_id': season1.pk})
    response = client.get(path, follow=True)
    assertTemplateUsed(response, 'users/ManagersListCatSeason.html')
