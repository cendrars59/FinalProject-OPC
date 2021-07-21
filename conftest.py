import pytest
from selenium import webdriver
from club.models import Category, EventType, Season, Division, Club
from practice.models import Practice, Skill
from users.models import CustomUser
from training_session.models import TrainingSession


@pytest.fixture()
def driver_init(request):
    """Fixture to use in the context of testing with Selenium. 
    Here the purpose is to test with Chrome on diffrent screen size

    Args:
        request ([type]): [description]
    """

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    web_driver = webdriver.Chrome(options=options)
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


@pytest.fixture()
def practice1(db):
    """
        This fixture is used to generate a dummy valid practice for Practice model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    practice = Practice.objects.create(label='bobo toto', description='practice dummy_description1')
    practice.save()
    return practice


@pytest.fixture()
def practice2(db):
    """
        This fixture is used to generate a dummy valid practice for Practice model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    practice = Practice.objects.create(label='practice2', description='practice dummy_description2')
    practice.save()
    return practice


@pytest.fixture()
def practice3(db):
    """
        This fixture is used to generate a dummy valid practice for Practice model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    practice = Practice.objects.create(label='practice3', description='practice dummy_description1')
    practice.save()
    return practice


@pytest.fixture()
def skill1(db):
    """
        This fixture is used to generate a dummy valid event_type for Season model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    skill = Skill.objects.create(label='Skill-dummy_label1',
                                 description='Skill dummy description1')
    skill.save()
    return skill


@pytest.fixture()
def skill2(db):
    """
        This fixture is used to generate a dummy valid event_type for Season model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    skill = Skill.objects.create(label='Skill-dummy_label2',
                                 description='Skill dummy description2')
    skill.save()
    return skill


@pytest.fixture()
def user1(db):
    """
        This fixture is used to generate a dummy valid event_type for Custom User model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    user = CustomUser.objects.create_user(
        email='email@user1.com',
        username='user1',
        first_name='fn user1',
        last_name='ln user1',
        address1='10 rue Parker Lewis',
        address2='Somewhere',
        zip_code=75000,
        city='New York',
        country='fr',
        mobile_phone='+336000000',
        password='totor'
    )
    return user


@pytest.fixture()
def training_session1(db, skill1, skill2, category2,
 category3,practice1, practice2, practice3):
    """
        This fixture is used to generate a dummy valid event_type for TrainingSession model validation
        The db parameter is equivalent to  @pytest.mark.django_db allowing the access to the 
        test database
        """
    training_session = TrainingSession.objects.create(
        label='training session dummy_label1',
        description='training session dummy description1',
        is_active=True,
        minimum_number_of_people=10,
        required_materials = 'training session dummy list of material'
    )
    training_session.skills.set([skill1.pk, skill2.pk]),
    training_session.practices.set([practice1.pk, practice2.pk, practice3.pk])
    training_session.categories.set([category2.pk, category3.pk])
    return training_session
