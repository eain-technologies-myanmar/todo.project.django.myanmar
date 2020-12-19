from django import forms # form သုံးချင်လို့ ကြေညာတယ်
from django.forms import ModelForm #ModelForm ကို ယူသုံးမယ်

from .models import Task # models.py ထဲမှ Task ကို ယူသုံးပါမယ်

class TaskForm(forms.ModelForm):
	title=forms.CharField(widget=forms.TextInput(attrs={'class': 'input','placeholder':'ရေးသားပါ'}))
	class Meta:
		model = Task 
		fields= '__all__' #အချက်အားလုံးကို ယူသုံးမယ်
