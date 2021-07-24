from django.contrib import admin 
from django.urls import path 
from movie.views import * 

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', home, name="home"),
    path('init_db/', init_db, name='init_db'),
    path('index/', index, name='index')
]
