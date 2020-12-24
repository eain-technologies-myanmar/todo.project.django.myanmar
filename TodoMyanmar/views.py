_B='form'
_A='POST'
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
def index(request):
	B=request;C=Task.objects.order_by('complete');A=TaskForm()
	if B.method==_A:
		A=TaskForm(B.POST)
		if A.is_valid():A.save()
		return redirect('/')
	D={'tasks':C,_B:A};return render(B,'index.html',D)
def updateTask(request,pk):
	B=request;C=Task.objects.get(id=pk);A=TaskForm(instance=C)
	if B.method==_A:
		A=TaskForm(B.POST,instance=C)
		if A.is_valid():A.save();return redirect('/')
	D={_B:A};return render(B,'update_task.html',D)
def deleteTask(request,pk):
	A=request;B=Task.objects.get(id=pk)
	if A.method==_A:B.delete();return redirect('/')
	C={'item':B};return render(A,'delete_task.html',C)