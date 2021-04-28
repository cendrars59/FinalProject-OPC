import pytest
from django import urls

# testing routing for each url to the correct views
# belonging to the pages app
# 200 is expected response from GET request
# Here we are testing the urls in the list passed as param
@pytest.mark.parametrize('param', [('home'), ('information'), ('legal')])
def test_render_pages_views(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200
