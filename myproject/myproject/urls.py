from django.contrib import admin 
from django.urls import path 
from movie.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name ='home'),
    path('detail/<str:id>', detail, name='detail'),
    path('init_db/', init_db, name='init_db'),
    path('login/', login_view, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('comment/<str:id>/', comment, name='comment')
]
