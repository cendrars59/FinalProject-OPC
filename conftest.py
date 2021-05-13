import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome1920", "chrome411"], scope="class")
def driver_init(request):
    """Fixture to use in the context of testing with Selenium. 
    Here the purpose is to test with Chrome on diffrent screen size

    Args:
        request ([type]): [description]
    """
    if request.param == "chrome1920":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        web_driver = webdriver.Chrome(options=options)
        request.cls.browser = "Chrome1920x1080"
    if request.param == "chrome411":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=411,823")
        web_driver = webdriver.Chrome(options=options)
        request.cls.browser = "Chrome411x823"
    request.cls.driver = web_driver
    yield
    web_driver.close()
