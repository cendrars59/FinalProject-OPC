import pytest
from selenium import webdriver
from club.models import Category, EventType, Season, Division, Club


@pytest.fixture(params=["chrome1920", "chrome411"])
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


@pytest.fixture()
def club1(db):
    """
        This fixture is used to generate a dummy valid club for Club model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    club = Club.objects.create(code='code-club1', label='club dummy_label1',
                               description='club dummy description1',
                               address='Address club 1',
                               main_phone='0123456789',
                               main_email='Main email club 1',
                               main_contact='Main contact club 1')
    club.save()
    return club


@pytest.fixture()
def club2(db):
    """
        This fixture is used to generate a dummy valid club for Club model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    club = Club.objects.create(code='code-club2', label='club dummy_label2',
                               description='club dummy description2',
                               address='Address club 2',
                               main_phone='0113456789',
                               main_email='Main email club 2',
                               main_contact='Main contact club 2')
    club.save()
    return club


@pytest.fixture()
def category1(db):
    """
        This fixture is used to generate a dummy valid category for Category model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    category = Category.objects.create(code='EDR-Dummy', label='dummy_label',
                                       description='dummy description', tag='EDR')
    category.save()
    return category


@pytest.fixture()
def category2(db):
    """
        This fixture is used to generate a dummy valid category for Category model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    category = Category.objects.create(code='cat2', label='dummy_label2',
                                       description='dummy description2', tag='EDR')
    category.save()
    return category


@pytest.fixture()
def category3(db):
    """
        This fixture is used to generate a dummy valid category for Category model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    category = Category.objects.create(code='cat3', label='dummy_label3',
                                       description='dummy description3', tag='EDR')
    category.save()
    return category


# @pytest.fixture()
# def role1(db):
#     """
#         This fixture is used to generate a dummy valid role for Role model validation
#         The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the
#         test database
#         """
#     role = Role.objects.create(code='Role-Dummy-Code', label='Role-dummy_label',
#                                description='Role dummy description')
#     return role


@pytest.fixture()
def event_type1(db):
    """
        This fixture is used to generate a dummy valid event_type for EventType model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    event_type = EventType.objects.create(code='Event-Type-Dummy-Code', label='Event-Type-dummy_label',
                                          description='Event-Type dummy description', color_code='#FF0000')
    return event_type


@pytest.fixture()
def season1(db):
    """
        This fixture is used to generate a dummy valid event_type for Season model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    season = Season.objects.create(code='Season-Dummy-Code', label='Season-dummy_label',
                                   description='Season dummy description', yob=2020, yoe=2021)
    season.save()
    print(season.pk)
    return season


@pytest.fixture()
def season2(db):
    """
        This fixture is used to generate a dummy valid event_type for Season model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    season = Season.objects.create(code='Season-Dummy-Code2', label='Season-dummy_label2',
                                   description='Season dummy description2', yob=2021, yoe=2022)
    season.save()
    return season


@pytest.fixture()
def division1(db):
    """
        This fixture is used to generate a dummy valid event_type for Division model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    division = Division.objects.create(code='Division-Dummy-Code', label='Division-dummy_label',
                                       description='Division dummy description')
    return division
