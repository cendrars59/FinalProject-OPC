import pytest
from training_plan.models import TrainingPlan


@pytest.mark.django_db
def test_training_plan_creation_according_model(training_plan1, category2, training_session1):
    # verify that the object is created
    assert TrainingPlan.objects.count() == 1
    assert training_plan1.code != ''
    assert training_plan1.label == 'training plan dummy_label1'
    assert training_plan1.description == 'training plan dummy description1'
    assert training_plan1.is_canceled == False
    assert training_plan1.required_materials == 'Un tutu et un chapeau pointu'
    assert training_plan1.category == category2
    assert training_plan1.training_session == training_session1