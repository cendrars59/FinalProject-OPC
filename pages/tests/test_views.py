import pytest
from django import urls
from pytest_django.asserts import assertTemplateUsed

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
    response = client.get(temp_url)
    assert response.status_code == 302
    assertTemplateUsed(response, f'pages/{param}.html')
