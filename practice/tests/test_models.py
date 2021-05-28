import pytest
from practice import models


def test_practice_object_creation_according_model(practice1, category3):
    # verify that the object is created
    assert practice1.code != ''
    assert practice1.label == 'bobo toto'
    assert practice1.description == 'practice dummy_description1'
    assert str(practice1) == practice1.label
    # adding test for logo later
    # adding test for manager later


def test_skill_object_creation_according_model(skill1):
    # verify that the object is created
    assert skill1.code != ''
    assert skill1.label == 'Skill-dummy_label1'
    assert skill1.description == 'Skill dummy description1'
    assert skill1.is_active == True
    assert str(skill1) == skill1.label
