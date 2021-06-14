from django.test import RequestFactory
from mixer.backend.django import mixer
import pytest
from django import urls
from users.models import CustomUser
from pytest_django.asserts import assertTemplateUsed
from pages.views import legal, information, home

# testing routing for each url to the correct views
# belonging to the pages app
# 200 is expected response from GET request
# and verify also that the right template is returned
# Here we are testing the urls in the list passed as param
@pytest.mark.parametrize('param', [('home'), ('information'), ('legal')])
def test_render_pages_views(client, param):
    # In onder to avoid the explicit url because it can change
    # we use reverse function to pass the name of the urls to get the full path
    temp_url = urls.reverse(param)
    request = RequestFactory().get(temp_url)
    request.user = mixer.blend(CustomUser)
    response = param(request)
    assert response.status_code == 302
    assertTemplateUsed(response, f'pages/{param}.html')
