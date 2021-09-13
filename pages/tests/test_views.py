from django.test import RequestFactory
#from mixer.backend.django import mixer
import pytest
from django import urls
from users.models import CustomUser
from pytest_django.asserts import assertTemplateUsed
from pages.views import legal, information, home
from django.urls.base import resolve

# testing routing for each url to the correct views
# belonging to the pages app
# 200 is expected response from GET request
# and verify also that the right template is returned
# Here we are testing the urls in the list passed as param


@pytest.mark.parametrize('param', [('home'), ('information'), ('legal')])
def test_render_pages_views(client, user1, param):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    client.login(username=user1.username, password="totor")
    path = urls.reverse(param)
    response = client.get(path)
    assert response.status_code == 200


@pytest.mark.parametrize('param', [('home'), ('information'), ('legal')])
def test_template_pages_views(client, user1, param):
    client.login(username=user1.username, password="totor")
    path = urls.reverse(param)
    response = client.get(path)
    assertTemplateUsed(response, f'pages/{param}.html')
