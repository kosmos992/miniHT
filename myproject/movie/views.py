from django.db import models
from django.shortcuts import render, redirect
from .models import Movie, Staff
import requests

def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

def init_db(request):
    url = "http://3.36.240.145:3479/mutsa"
    res = requests.get(url)
    movies = res.json()['movies']
    print(movies)
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
        print(staff)

    return redirect('index')