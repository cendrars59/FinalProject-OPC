from django import forms
from training_plan.models import TrainingPlan
from ckeditor.widgets import CKEditorWidget


class AddForm(forms.ModelForm):
    """
    class in order to manage the adding of a
    new practice 
    """
    
    class Meta:
        model = TrainingPlan
        fields = ('label','description','is_canceled')

        widgets = {
        
        }