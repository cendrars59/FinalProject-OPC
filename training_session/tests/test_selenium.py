import time
import pytest
from users.models import CustomUser
from selenium.webdriver.common.by import By

pytestmark = pytest.mark.django_db


@pytest.mark.usefixtures("driver_init")
class TestPracticesPages:

    @pytest.mark.django_db
    def test_training_session_list(self, live_server, driver_init, user1, user1_involved_in_season1_as_manager):

        self.driver.get(("%s" % (live_server.url)))
        time.sleep(2)
        # Verify the redirection to the login page if user is not connected
        assert self.driver.current_url == live_server.url + "/login/?next=/"
        assert "Login" in self.driver.title
        self.driver.find_element_by_name("username").send_keys(user1.email)
        self.driver.find_element_by_name("password").send_keys("totor")
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(2)
        self.driver.find_element_by_id("dbkt_link_menu").click()
        time.sleep(2)
        self.driver.find_element_by_id("trainingsession_list_link").click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url + "/training_sessions/"
        assert "Liste d'entrainements type" in self.driver.title

    @pytest.mark.django_db
    def test_training_session_detail(self, live_server, driver_init, user1, training_session1, user1_involved_in_season1_as_manager):

        self.driver.get(("%s" % (live_server.url)))
        time.sleep(2)
        # Verify the redirection to the login page if user is not connected
        assert self.driver.current_url == live_server.url + "/login/?next=/"
        assert "Login" in self.driver.title
        self.driver.find_element_by_name("username").send_keys(user1.email)
        self.driver.find_element_by_name("password").send_keys("totor")
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(2)
        self.driver.find_element_by_id("dbkt_link_menu").click()
        time.sleep(2)
        self.driver.find_element_by_id("trainingsession_list_link").click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url + "/training_sessions/"
        id = f"{training_session1.id}_details"
        self.driver.find_element_by_id(id).click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url + f"/training_sessions/{training_session1.id}/"
        self.driver.find_element_by_id('trainingsession_description_link').click()
        time.sleep(1)
        self.driver.find_element_by_id('trainingsession_skills_link').click()
        time.sleep(1)
        self.driver.find_element_by_id('trainingsession_categories_link').click()
        time.sleep(1)
        self.driver.find_element_by_id('trainingsession_practices_link').click()
        time.sleep(1)
