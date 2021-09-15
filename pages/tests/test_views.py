from django.test import RequestFactory
#from mixer.backend.django import mixer
import pytest
from django import urls
from users.models import CustomUser
from pytest_django.asserts import assertTemplateUsed
from pages.views import legal, information, home
from django.urls.base import resolve


@pytest.mark.parametrize('param', [('home'), ('information'), ('legal')])
@pytest.mark.django_db
def test_render_pages_views(client, user1, category1, user1_involved_in_season1_as_manager, param):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.login(username=user1.email, password="totor")
    path = urls.reverse(param)
    response = client.get(path, follow=True)
    assert response.status_code == 200


@pytest.mark.parametrize('param', [('home'), ('information'), ('legal')])
@pytest.mark.django_db
def test_template_pages_views(client, user1, category1, user1_involved_in_season1_as_manager, param):
    client.login(username=user1.email, password="totor")
    path = urls.reverse(param)
    response = client.get(path, follow=True)
    assertTemplateUsed(response, f'pages/{param}.html')
