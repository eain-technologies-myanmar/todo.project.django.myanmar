from django.contrib import admin

# Register your models here.
from .models import Task # models.py ထဲမှ class Task ကို ယူသုံးမယ် 

admin.site.register(Task) # admin panel တွင် ပေါ်ရန် ရေးသားခြင်း
