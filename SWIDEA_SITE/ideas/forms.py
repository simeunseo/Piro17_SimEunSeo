from django import forms
from .models import Idea, Tool
        
class IdeaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)
        self.fields['tool'].required = True
        self.fields['image'].required = True
        
    class Meta:
        model = Idea
        fields = ['name','image','description','interest','tool']
