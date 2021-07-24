from django.db import models
from django.shortcuts import get_object_or_404, render, redirect
from .models import Movie, Staff, Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth
from .forms import SignupForm
import requests
from django.core.paginator import Paginator



def home(request):
    movies = Movie.objects.all()
#    staff = Staff.objects.all()
    paginator = Paginator(movies, 3) # blogs를 3개씩 쪼갠다
    page = request.GET.get('page') # 해당 정보가 오지 않아도 넘어간다
    paginated_movies = paginator.get_page(page)
    return render(request, 'home.html', {'movies': paginated_movies})

def detail(request, id):
  movie = get_object_or_404(Movie, pk = id)
  comment = Comment.objects.filter(movie=movie)
  staff = Staff.objects.filter(movie=movie)

  return render(request, 'detail.html', {'movie':movie, 'comment':comment, 'staff': staff})

def init_db(request):
    url = "http://3.36.240.145:3479/mutsa"
    res = requests.get(url)
    movies = res.json()['movies']

    for movie in movies:
        mv = Movie()
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
            staff = Staff()
            staff.name = s['name']
            staff.role = s['role']
            staff.image_url = s['image_url']
            staff.movie = mv
            staff.save()

    return redirect('home')

def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = auth.authenticate(
        request=request,
        username=username,
        password=password
      )

      if user is not None:
        auth.login(request, user)
        return redirect('home')

    return redirect('login')
  
  else:
    form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form})

def logout(request):
	auth.logout(request)
	return redirect('home')

def signup_view(request):
  if request.method == 'POST':
    form = SignupForm(request.POST) 
    if form.is_valid():
      user = form.save()
      auth.login(request, user)
      return redirect('home')
    return redirect('signup')
    
  else:
    form = SignupForm()
    return render(request, 'signup.html', {'form' : form})

def comment(request, id):
    comment = Comment()
    comment.body = request.POST['body']
    movie = get_object_or_404(Movie, pk = id)
    comment.movie = movie
    if request.user.is_authenticated:
        comment.user = request.user
    else: 
      return redirect('login')
    comment.save()
    return redirect('detail',id)
