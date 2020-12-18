from django.shortcuts import render,redirect
from django.http import HttpResponse # HttpReponse ကိုသုံးချင်လို့ import လုပ်ပြီး သုံးပါတယ် 
from .models import Task # models.py ထဲမှ Task ကို ယူသုံးပါမယ်
from .forms import TaskForm # forms.py မှ TaskForm ကို ခေါ်သုံးပါမယ်
# Create your views here.
def index(request):
	#return HttpResponse('<h1>လုပ်ဆောင်</h1>') # ပေါ်ချင်တာ ရေးပြီးတဲ့အခါ လက်တွေလုပ်ဆောင်နိုင်ရန် urls.py တွင် ကြေညာ၍ အသုံးပြုရမယ်
	#return render(request,"index.html",{})
	tasks=Task.objects.all()
	form =TaskForm() #forms.py က TaskForm ကို ​form ထဲထည့်

	if request.method == 'POST': # data ထည့်တာ ရှိခဲ့ရင်
		form = TaskForm(request.POST) 
		if form.is_valid(): # မှန်ရင် save
			form.save()
		return redirect('/') # ပြီးမှ မူလစာမျက်နှာကို ပြန်ခေါ်
	context={'tasks':tasks,'form':form}
	return render(request,'index.html',context) # index page သို့ database မှအချက်အလက်များ ပို့ဆောင်
def updateTask(request,pk):
	task=Task.objects.get(id=pk)
	form=TaskForm(instance=task)
	if request.method=='POST':
		form=TaskForm(request.POST,instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form':form}
	return render(request,'update_task.html',context)
def deleteTask(request,pk):
	item=Task.objects.get(id=pk)
	if request.method=='POST':
		item.delete()
		return redirect('/')
	context={'item':item}
	return render(request,'delete_task.html',context)