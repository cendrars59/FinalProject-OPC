import time
import pytest
from users.models import CustomUser
from selenium.webdriver.common.by import By

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


    def test_practice_detail(self, live_server,driver_init, user1, practice1, practice2):

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


    
    def test_practice_creation(self, live_server,driver_init, user1):

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
        self.driver.find_element_by_id("new-practice-list").click()
        time.sleep(2)
        assert self.driver.current_url == live_server.url +"/practices/new/"
        # Use to interact ckeditor
        # https://stackoverflow.com/questions/49603312/interacting-with-ckeditor-in-selenium-python 
        self.driver.find_element_by_name("label").send_keys("Dummy Practice Label")
        frame = self.driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame')
        self.driver.switch_to.frame(frame)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys("""Qu'est-ce que le Lorem Ipsum?
Le Lorem Ipsum est simplement du faux texte employé dans la composition
 et la mise en page avant impression.
  Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500,
   quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser
    un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles,
     mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié.
      Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum,
       et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker.""")