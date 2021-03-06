import time
import pytest
from users.models import CustomUser
from selenium.webdriver.common.by import By

pytestmark = pytest.mark.django_db


@pytest.mark.usefixtures("driver_init")
class TestPracticesPages:

    @pytest.mark.django_db
    def test_practices_list(self, live_server, driver_init, user1, user1_involved_in_season1_as_manager, practice1, practice2):

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
        self.driver.find_element_by_id("practices_list_link").click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url + "/practices/"
        assert "Liste d'exercices" in self.driver.title

    @pytest.mark.django_db
    def test_practice_detail(self, live_server, driver_init, user1, user1_involved_in_season1_as_manager, practice1, practice2):

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
        self.driver.find_element_by_id("practices_list_link").click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url + "/practices/"
        id = f"{practice1.id}_details"
        self.driver.find_element_by_id(id).click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url + f"/practices/{practice1.id}/"
        self.driver.find_element_by_id('practice_description_link').click()
        time.sleep(1)
        self.driver.find_element_by_id('practice_skills_link').click()
        time.sleep(1)
        self.driver.find_element_by_id('practice_categories_link').click()
        time.sleep(1)

    @pytest.mark.django_db
    def test_practice_creation(self, live_server, driver_init, user1, user1_involved_in_season1_as_manager):

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
        self.driver.find_element_by_id("practices_list_link").click()
        time.sleep(2)
        self.driver.find_element_by_id("new-practice-list").click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url + "/practices/new/"
        # Use to interact ckeditor
        # https://stackoverflow.com/questions/49603312/interacting-with-ckeditor-in-selenium-python
        self.driver.find_element_by_name("label").send_keys("Dummy Practice Label")
        frame = self.driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame')
        self.driver.switch_to.frame(frame)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys("""Qu'est-ce que le Lorem Ipsum?
Le Lorem Ipsum est simplement du faux texte employ?? dans la composition
 et la mise en page avant impression.
  Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les ann??es 1500,
   quand un imprimeur anonyme assembla ensemble des morceaux de texte pour r??aliser
    un livre sp??cimen de polices de texte. Il n'a pas fait que survivre cinq si??cles,
     mais s'est aussi adapt?? ?? la bureautique informatique, sans que son contenu n'en soit modifi??.
      Il a ??t?? popularis?? dans les ann??es 1960 gr??ce ?? la vente de feuilles Letraset contenant des passages du Lorem Ipsum,
       et, plus r??cemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker.""")
