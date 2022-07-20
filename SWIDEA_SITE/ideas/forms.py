from django import forms
from .models import Idea, Tool

# tool = Tool.objects.all()
# TOOL_CHOICES = [(None,'------')]
# for t in tool:
#     temp = []
#     temp.append(t.name)
#     temp.append(t.name)
#     temp = tuple(temp)
#     TOOL_CHOICES.append(temp)
# TOOL_CHOICES=tuple(TOOL_CHOICES)
        
class IdeaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)
        self.fields['tool'].required = True
        
    class Meta:
        model = Idea
        fields = ['name','image','description','interest','tool']
