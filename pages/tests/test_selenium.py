import pytest
from django.test import LiveServerTestCase  # Use to run a websrver for testing purpose.
from selenium import webdriver


class TestPages(LiveServerTestCase):

    def test_example(self):
        driver = webdriver.Chrome()
        driver.get(("%s%s" % (self.live_server_url, "/legal")))
        assert "Mentions légales" in driver.title
