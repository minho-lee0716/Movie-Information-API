from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ObjectDoesNotExist

from .models import (
    Movie,
    Genre,
    MovieRating,
    Actor,
    Director,
    MovieActor,
    MovieDirector
)

class AllMovieView(View):
    def get(self, request):
        try:
            if len(Movie.objects.all()) == 0:
                return JsonResponse({'data':[]}, status=200)

            movies = [{
                'movie_no'          : movie.movie_no,
                'poster_img'        : movie.poster_img,
                'name'              : movie.name,
                'star_rating'       : float(movie.star_rating),
                'openning_date'     : movie.openning_date,
                'number_of_viewers' : movie.number_of_viewers
            } for movie in Movie.objects.all()]
            return JsonResponse({'data':movies}, status=200)

        except Exception as e:
            return JsonResponse({'message':f'{e}'}, status=400)

class DetailMovieView(View):
    def get(self, request, movie_no):
        try:
            actors    = list(Movie.objects.prefetch_related('actor_set').get(movie_no=movie_no).actor_set.values_list('name', flat=True))
            directors = list(Movie.objects.prefetch_related('director_set').get(movie_no=movie_no).director_set.values_list('name', flat=True))
            movie_obj = Movie.objects.select_related('genre', 'movie_rating').get(movie_no=movie_no)

            movie = {
                'movie_no'               : movie_obj.movie_no,
                'poster_img'             : movie_obj.poster_img,
                'name'                   : movie_obj.name,
                'star_rating'            : float(movie_obj.star_rating),
                'openning_date'          : movie_obj.openning_date,
                'number_of_viewers'      : movie_obj.number_of_viewers,
                'country_of_manufacture' : movie_obj.country_of_manufacture,
                'genre'                  : movie_obj.genre.name,
                'movie_rating'           : movie_obj.movie_rating.name,
                'running_time'           : movie_obj.running_time,
                'directors'              : actors,
                'actors'                 : directors,
                'summary'                : movie_obj.summary
            }
            return JsonResponse({'data':movie}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'message':'Movie information that does not exist'}, status=400)

#        except KeyError:
#            return JsonResponse({'message':'Query params type error'}, status=400)

        except Exception as e:
            return JsonResponse({'message':f'{e}'}, status=400)
