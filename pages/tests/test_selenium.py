import time
import pytest
from users.models import CustomUser

pytestmark = pytest.mark.django_db


class TestPageLegal:

    @pytest.mark.django_db
    @pytest.mark.usefixtures("driver_init")
    def test_legal_page(self, live_server, driver_init, user1, user1_involved_in_season1_as_manager):

        self.driver.get(("%s%s" % (live_server.url, "/legal")))
        time.sleep(2)
        # Verify the redirection to the login page if user is not connected
        assert self.driver.current_url == live_server.url + "/login/?next=/legal"
        assert "Login" in self.driver.title
        self.driver.find_element_by_name("username").send_keys(user1.email)
        self.driver.find_element_by_name("password").send_keys("totor")
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url + "/legal"
        assert self.driver.find_element_by_id("legal-p1").text != ""
        assert self.driver.find_element_by_id("legal-p2").text != ""
        assert self.driver.find_element_by_id("legal-p3").text != ""
        assert self.driver.find_element_by_id("legal-p4").text != ""
        assert self.driver.find_element_by_id("legal-p5").text != ""
        assert self.driver.find_element_by_id("legal-p6").text != ""
        assert self.driver.find_element_by_id("legal-p7").text != ""


class TestPageHome:

    @pytest.mark.django_db
    @pytest.mark.usefixtures("driver_init")
    def test_home_page(self, live_server, driver_init, user1, user1_involved_in_season1_as_manager):

        self.driver.get(("%s%s" % (live_server.url, "/login")))
        time.sleep(2)
        # Verify the redirection to the login page if user is not connected
        assert "Login" in self.driver.title
        self.driver.find_element_by_name("username").send_keys(user1.email)
        self.driver.find_element_by_name("password").send_keys("totor")
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url + "/"
