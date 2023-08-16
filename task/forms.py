from django import forms
from django.forms import ModelForm

from task.models import Task, Profile


class CreateTaskForm(ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 
                  'status', 'executor', 
                  'check', 'published']
        
    # def __init__(self, *args, **kwargs):
    #     super(CreateTaskForm, self).__init__(*args, **kwargs)
    #     self.fields['description'].required = False


