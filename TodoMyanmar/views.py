from django.shortcuts import render
from django.http import HttpResponse # HttpReponse ကိုသုံးချင်လို့ import လုပ်ပြီး သုံးပါတယ် 

# Create your views here.
def index(request):
	return HttpResponse('<h1>လုပ်ဆောင်</h1>') # ပေါ်ချင်တာ ရေးပြီးတဲ့အခါ လက်တွေလုပ်ဆောင်နိုင်ရန် urls.py တွင် ကြေညာ၍ အသုံးပြုရမယ်