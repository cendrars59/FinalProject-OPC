import time
import pytest
from users.models import CustomUser

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
@pytest.mark.usefixtures("driver_init")
class TestPracticesPages:

    def test_practices_list(self, live_server,driver_init, user1, practice1, practice2):

        self.driver.get(("%s" % (live_server.url)))
        time.sleep(2)
        # Verify the redirection to the login page if user is not connected 
        assert self.driver.current_url == live_server.url +"/login/?next=/"
        assert "Login" in self.driver.title
        self.driver.find_element_by_name("username").send_keys(user1.email)
        self.driver.find_element_by_name("password").send_keys("totor")
        self.driver.find_element_by_tag_name("button").click()
        time.sleep(2)
        self.driver.find_element_by_id("dbkt_link_menu").click()
        time.sleep(2)
        self.driver.find_element_by_id("practices_list_link").click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url +"/practices/"
        assert "Liste d'exercices" in self.driver.title


    
    # def test_practice_creation(self, live_server,driver_init, user1, skill1, category1, category2, category3):

    #     self.driver.get(("%s" % (live_server.url)))
    #     time.sleep(2)
    #     # Verify the redirection to the login page if user is not connected 
    #     assert self.driver.current_url == live_server.url +"/login/?next=/"
    #     assert "Login" in self.driver.title
    #     self.driver.find_element_by_name("username").send_keys(user1.email)
    #     self.driver.find_element_by_name("password").send_keys("totor")
    #     self.driver.find_element_by_tag_name("button").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_id("dbkt_link_menu").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_id("practices_list_link").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_id("new-practice-list").click()
    #     time.sleep(2)
    #     assert self.driver.current_url == live_server.url +"/practices/new/"
    #     self.driver.find_element_by_name("label").send_keys("Dummy Practice Label")
    #     self.driver.find_element_by_name("description").send_keys("Dummy Practice Description")