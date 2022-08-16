from .models import Movie
from rest_framework.response import Response
from .serializers import MovieSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method=="GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    if request.method=="POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method=="GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    if request.method=="PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method=="DELETE":
        movie.delete()
        return Response("Item Deleted!")
        


