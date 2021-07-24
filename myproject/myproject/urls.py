from django.contrib import admin 
from django.urls import path 
from movie import views 

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name="home"),
    path('init_db/', init_db, name='init_db')
]