from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    movies = Movies.objects.all()
    error_message=''
    #search functionality
    movie_name = request.GET.get('movie_name')

    if movie_name != '' and movie_name is not None:
        movies = movies.filter(name__icontains=movie_name)

        if not movies:
            error_message="Movie not Found"
    

    paginator = Paginator(movies,2)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    return render(request,'pagination/movies_list.html',{'movies':movies, 'error_message':error_message})

