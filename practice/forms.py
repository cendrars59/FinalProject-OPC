from django import forms
from practice.models import Practice
from ckeditor.widgets import CKEditorWidget


class AddForm(forms.ModelForm):
    """
    class in order to manage the adding of a
    new practice 
    """
    
    class Meta:
        model = Practice
        fields = ('label','description','is_active','categories','skills')

        widgets = {
        
        }