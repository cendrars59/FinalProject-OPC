import pytest
from training_session.models import TrainingSession


@pytest.mark.django_db
def test_training_session_creation_according_model(training_session1):
    # verify that the object is created
    assert TrainingSession.objects.count() == 1
    assert training_session1.code != ''
    assert training_session1.label == 'training session dummy_label1'
    assert training_session1.description == 'training session dummy description1'
    assert training_session1.is_active == True
    assert training_session1.minimum_number_of_people == 10
    assert training_session1.required_materials == 'training session dummy list of material'
