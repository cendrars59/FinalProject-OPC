import pytest


@pytest.mark.usefixtures("driver_init")
class TestPages:

    def test_example(self, live_server):

        self.driver.get(("%s%s" % (live_server.url, "/legal")))

        assert "Mentions légales" in self.driver.title
        assert self.driver.find_element_by_id("legal-p1").text != ""
        assert self.driver.find_element_by_id("legal-p2").text != ""
        assert self.driver.find_element_by_id("legal-p3").text != ""
        assert self.driver.find_element_by_id("legal-p4").text != ""
        assert self.driver.find_element_by_id("legal-p5").text != ""
        assert self.driver.find_element_by_id("legal-p6").text != ""
        assert self.driver.find_element_by_id("legal-p7").text != ""
