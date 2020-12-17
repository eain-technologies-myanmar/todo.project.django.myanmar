from django.shortcuts import render
from django.http import HttpResponse # HttpReponse ကိုသုံးချင်လို့ import လုပ်ပြီး သုံးပါတယ် 
from .models import Task

# Create your views here.
def index(request):
	#return HttpResponse('<h1>လုပ်ဆောင်</h1>') # ပေါ်ချင်တာ ရေးပြီးတဲ့အခါ လက်တွေလုပ်ဆောင်နိုင်ရန် urls.py တွင် ကြေညာ၍ အသုံးပြုရမယ်
	#return render(request,"index.html",{})
	tasks=Task.objects.all()

	context={'tasks':tasks}
	return render(request,'index.html',context) # index page သို့ database မှအချက်အလက်များ ပို့ဆောင်