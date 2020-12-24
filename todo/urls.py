from django.contrib import admin
from django.urls import path
from TodoMyanmar.views import index,updateTask,deleteTask
urlpatterns=[path('admin/',admin.site.urls),path('',index,name='index'),path('update/<str:pk>/',updateTask,name='update_task'),path('delete/<str:pk>/',deleteTask,name='delete_task')]