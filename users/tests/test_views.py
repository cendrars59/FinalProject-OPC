import pytest
from django.urls import reverse


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
