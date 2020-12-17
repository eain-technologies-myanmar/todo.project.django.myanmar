from django.db import models

# Create your models here.
class Task(models.Model):
	title=models.CharField(max_length=200) # စာလုံးရေ ၂၀၀ အထိ ရေးသားနိုင်သော လုပ်ဆောင်ချက် ခေါင်းစဥ်
	complete=models.BooleanField(default=False) # လုပ်ဆောင်ချက် ပြီးမြောက်ကြောင်း ဖော်ပြနိုင်ရန် အမှန်(သို့မဟုတ်)အမှား သတ်မှတ်ချက်
	create = models.DateTimeField(auto_now_add=True) # လုပ်ဆောင်ချက်အား မည်သည့်အချိန်တွင် လုပ်ဆောင်ခဲ့သည်ကို သတ်မှတ်ရန် အသုံးပြု

	def __str__(self):
		return self.title