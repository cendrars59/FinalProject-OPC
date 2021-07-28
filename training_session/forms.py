from django import forms
from training_session.models import TrainingSession
from ckeditor.widgets import CKEditorWidget


class AddForm(forms.ModelForm):
    """
    class in order to manage the adding of a
    new session to plan 
    """
    
    class Meta:
        model = TrainingSession
        fields = ('label','description','is_active','practices','categories','skills')

        widgets = {
        
        }