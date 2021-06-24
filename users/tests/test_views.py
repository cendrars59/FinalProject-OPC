import pytest


# client fixture to emalute browser
def test_with_authenticated_client(client, user1):
    client.force_login(user1)
    response = client.get('/')
    content = response.content.decode(response.charset)
    # Verify that the user is connected and his or her first name is displayed on the page 
    assert response.status_code == 200
    assert '<a id="url-legal" class="text-muted" href="/legal">Legal</a>' in content
    assert 'href="https://www.rugby-tourcoing.com/"' in content

