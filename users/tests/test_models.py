from users import models
import pytest


def test_user_object_creation_according_model(user1):
    assert user1.email == 'email@user1.com'
    assert user1.username=='user1'
    assert user1.first_name == 'fn user1'
    assert user1.last_name == 'ln user1'
    assert user1.date_of_birth==None
    assert user1.address1== '10 rue Parker Lewis'
    assert user1.address2== 'Somewhere'
    assert user1.zip_code==75000
    assert user1.city=='New York'
    assert user1.country == 'FR'
    assert user1.mobile_phone == '+336000000'
    assert user1.phone_for_whatsapp == False
    # adding test for logo later
    # adding test for manager later