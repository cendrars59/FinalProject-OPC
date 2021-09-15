import time
import pytest
from users.models import CustomUser

pytestmark = pytest.mark.django_db


@pytest.mark.usefixtures("driver_init")
class TestUserLogin:
    @pytest.mark.django_db
    def test_login_page_sucess(self, live_server, driver_init, user1, user1_involved_in_season1_as_manager):

        self.driver.get(("%s" % (live_server.url)))
        time.sleep(2)
        # Verify the redirection to the login page if user is not connected
        assert self.driver.current_url == live_server.url + "/login/?next=/"
        assert "Login" in self.driver.title
        self.driver.find_element_by_name("username").send_keys(user1.email)
        self.driver.find_element_by_name("password").send_keys("totor")
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url + "/"

    @pytest.mark.django_db
    def test_login_page_failed(self, live_server, driver_init, user1, user1_involved_in_season1_as_manager):

        self.driver.get(("%s" % (live_server.url)))
        time.sleep(2)
        # Verify the redirection to the login page if user is not connected
        assert self.driver.current_url == live_server.url + "/login/?next=/"
        assert "Login" in self.driver.title
        self.driver.find_element_by_name("username").send_keys(user1.email)
        self.driver.find_element_by_name("password").send_keys("elvis")
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url + "/login/?next=/"


@pytest.mark.django_db
@pytest.mark.usefixtures("driver_init")
class TestUserLogout:

    def test_logout_page_sucess(self, live_server, driver_init, user1, user1_involved_in_season1_as_manager):

        self.driver.get(("%s" % (live_server.url)))
        time.sleep(2)
        # Verify the redirection to the login page if user is not connected
        assert self.driver.current_url == live_server.url + "/login/?next=/"
        assert "Login" in self.driver.title
        self.driver.find_element_by_name("username").send_keys(user1.email)
        self.driver.find_element_by_name("password").send_keys("totor")
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(2)
        self.driver.find_element_by_id("userDropdown").click()
        self.driver.find_element_by_id("logout_url").click()

        assert self.driver.current_url == live_server.url + "/logout/"
        assert "Logout" in self.driver.title


@pytest.mark.django_db
@pytest.mark.usefixtures("driver_init")
class TestUserProfil:

    def test_logout_page_sucess(self, live_server, driver_init, user1, user1_involved_in_season1_as_manager):

        self.driver.get(("%s" % (live_server.url)))
        time.sleep(2)
        # Verify the redirection to the login page if user is not connected
        assert self.driver.current_url == live_server.url + "/login/?next=/"
        assert "Login" in self.driver.title
        self.driver.find_element_by_name("username").send_keys(user1.email)
        self.driver.find_element_by_name("password").send_keys("totor")
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(2)
        self.driver.find_element_by_id("userDropdown").click()
        self.driver.find_element_by_id("profil_url").click()

        assert self.driver.current_url == live_server.url + "/edit/" + str(user1.id)
        assert "Votre compte" in self.driver.title
        assert self.driver.find_element_by_name("first_name").get_attribute('value') == user1.first_name
        assert self.driver.find_element_by_name("last_name").get_attribute('value') == user1.last_name
        assert self.driver.find_element_by_name("email").get_attribute('value') == user1.email
        assert self.driver.find_element_by_name("username").get_attribute('value') == user1.username
