from django import forms
from django.forms import ModelForm
from .models import Task
class TaskForm(forms.ModelForm):
	title=forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'ရေးသားပါ'}))
	class Meta:model=Task;fields='__all__'