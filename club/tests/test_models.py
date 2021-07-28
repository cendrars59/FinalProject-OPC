import pytest
from club import models


def test_club_object_creation_according_model(club1):
    # verify that the object is created
    assert models.Club.objects.count() == 1
    assert club1.code == 'code-club1'
    assert club1.label == 'club dummy_label1'
    assert club1.description == 'club dummy description1'
    assert club1.is_active == True
    assert club1.is_main == False
    assert club1.address == 'Address club 1'
    assert club1.main_phone == '0123456789'
    assert club1.main_email == 'Main email club 1'
    assert club1.main_contact == 'Main contact club 1'
    assert club1.main_color_code == ''
    assert str(club1) == club1.label
    # adding test for logo later
    # adding test for manager later


def test_category_object_creation_according_model(category1):
    # verify that the object is created
    assert models.Category.objects.count() == 1
    assert category1.code == 'EDR-Dummy'
    assert category1.label == 'dummy_label'
    assert category1.description == 'dummy description'
    assert category1.tag == 'EDR'
    assert category1.is_active == True
    assert str(category1) == category1.label
    # adding test for logo later
    # adding test for manager later


# def test_role_object_creation_according_model(role1): To move when creation members
#    # verify that the object is created
#    assert models.Role.objects.count() == 1
#    assert role1.code == 'Role-Dummy-Code'
#    assert role1.label == 'Role-dummy_label'
#    assert role1.description == 'Role dummy description'
#    assert role1.is_active == True
#    assert str(role1) == role1.label
#    # adding test for logo later


def test_event_type_object_creation_according_model(event_type1):
    # verify that the object is created
    assert models.EventType.objects.count() == 1
    assert event_type1.code == 'Event-Type-Dummy-Code'
    assert event_type1.label == 'Event-Type-dummy_label'
    assert event_type1.description == 'Event-Type dummy description'
    assert event_type1.color_code == '#FF0000'
    assert event_type1.is_active == True
    assert str(event_type1) == event_type1.label


def test_season_object_creation_according_model(season1):
    # verify that the object is created
    assert models.Season.objects.count() == 1
    assert season1.code == 'Season-Dummy-Code'
    assert season1.label == 'Season-dummy_label'
    assert season1.description == 'Season dummy description'
    assert season1.beg_date == '2021-09-01'
    assert season1.end_date == '2022-08-31'
    assert season1.is_active == True
   # assert season1.is_current == False
    assert str(season1) == season1.label


def test_division_object_creation_according_model(division1):
    # verify that the object is created
    assert models.Division.objects.count() == 1
    assert division1.code == 'Division-Dummy-Code'
    assert division1.label == 'Division-dummy_label'
    assert division1.description == 'Division dummy description'
    assert division1.is_active == True
    assert str(division1) == division1.label
