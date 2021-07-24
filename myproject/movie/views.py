from django.db import models
from django.shortcuts import render, redirect
from .models import Movie, Staff
import requests
from django.core.paginator import Paginator

def home(request):
    movies = Movie.objects.all()
#    staff = Staff.objects.all()
    paginator = Paginator(movies, 3) # blogs를 3개씩 쪼갠다
    page = request.GET.get('page') # 해당 정보가 오지 않아도 넘어간다
    paginated_movies = paginator.get_page(page)
    return render(request, 'home.html', {'movies': paginated_movies})


def index(request):
    movies = Movie.objects.all()
    staff = Staff.objects.all()
    return render(request, 'index.html', {'movies': movies, 'staff': staff})

def init_db(request):
    url = "http://3.36.240.145:3479/mutsa"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        mv = Movie()
        staff = Staff()
        mv.title_kor = movie['title_kor']
        mv.title_eng = movie['title_eng']
        mv.poster_url = movie['poster_url']
        mv.rating_aud = movie['rating_aud']
        mv.rating_cri = movie['rating_cri']
        mv.rating_net = movie['rating_net']
        mv.genre = movie['genre']
        mv.showtimes = movie['showtimes']
        mv.release_date = movie['release_date']
        mv.rate = movie['rate']
        mv.summary = movie['summary']
        mv.save()
        for s in movie['staff']:
            staff.name = s['name']
            staff.role = s['role']
            staff.image_url = s['image_url']
            staff.movie = mv
        staff.save()

    return redirect('index')
