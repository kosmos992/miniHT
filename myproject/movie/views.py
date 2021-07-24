from django.shortcuts import render

def home(request):
 #   movies = .objects.all()
    return render(request, 'home.html')
    #, {'movies', movies}