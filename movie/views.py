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

import json, datetime

class AllMovieView(View):
    def get(self, request):
        try:

            # 데이터가 없다면 빈 리스트를 반환해줍니다.
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

    def post(self, request):
        try:
            body          = json.loads(request.body)
            openning_date = body['openning_date'].split('-')
            genres        = list(Genre.objects.values_list('name', flat=True))
            movie_ratings = list(MovieRating.objects.values_list('name', flat=True))

            # POST 메소드로 body에 들어온 값들을 통해 movies 테이블에 정보 넣기
            new_movie_obj = Movie.objects.create(
                poster_img             = body['poster_img'],
                name                   = body['name'],
                star_rating            = body['star_rating'],
                openning_date          = body['openning_date'],
                number_of_viewers      = body['number_of_viewers'],
                country_of_manufacture = body['country_of_manufacture'],

                # genres table 관련
                # 삼항 연산자를 이용해 장르가 있다면 가져와서 넣고, 없다면 만들고 값을 넣어주기
                genre = (
                    Genre.objects.get(name=body['genre']).name if body['genre'] in genres else Genre.objects.create(name=body['genre'])
                ),

                # movie_ratings table 관련
                movie_rating = (
                    MovieRating.objects.get(name=body['movie_rating']).name if body['movie_rating'] in movie_ratings else MovieRating.objects.create(name=body['movie_rating'])
                ),

                running_time  = body['running_time'],
                summary       = body['summary']
            )

            # actors table and movies_actors table
            for actor in body['actors']:

                if actor in list(Actor.objects.values_list('name', flat=True)):

                    # movies_actors table
                    MovieActor.objects.create(
                        movie_id = new_movie_obj.movie_no,
                        actor_id = Actor.objects.get(name=actor).actor_no
                    )

                else:

                    # actors table
                    new_actor_obj = Actor.objects.create(name=actor)

                    # movies_actors table
                    MovieActor.objects.create(
                        movie_id = new_movie_obj.movie_no,
                        actor_id = new_actor_obj.actor_no
                    )

            # actors table and movies_actors table
            for director in body['directors']:

                if director in list(Director.objects.values_list('name', flat=True)):

                    # movies_directors table
                    MovieDirector.objects.create(
                        movie_id    = new_movie_obj.movie_no,
                        director_id = Director.objects.get(name=director).director_no
                    )

                else:

                    # directors table
                    new_director_obj = Director.objects.create(name=director)

                    # movies_directors table
                    MovieDirector.objects.create(
                        movie_id    = new_movie_obj.movie_no,
                        director_id = new_director_obj.director_no
                    )

            return JsonResponse({'message':'Success POST Method'}, status=200)

        except KeyError:
            return JsonResponse({'messaage':'KEY_ERROR'}, status=400)

        except TypeError:
            return JsonResponse({'message':'TYPE_ERROR'}, status=400)

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
                'directors'              : directors,
                'actors'                 : actors,
                'summary'                : movie_obj.summary
            }
            return JsonResponse({'data':movie}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'message':'It is a movie that does not exist.'}, status=400)

        #except KeyError:
        #    return JsonResponse({'message':'Query params type error'}, status=400)

        except Exception as e:
            return JsonResponse({'message':f'{e}'}, status=400)

    def put(self, request, movie_no):
        try:
            body      = json.loads(request.body)
            movie_obj = Movie.objects.get(movie_no=movie_no)

            # genre table
            if body['genre'] in list(Genre.objects.values_list('name', flat=True)):
                genre_obj = Genre.objects.get(name=body['genre'])
            else:
                genre_obj = Genre.objects.create(name=body['genre'])

            # movie_rating table
            if body['movie_rating'] in list(MovieRating.objects.values_list('name', flat=True)):
                movie_rating_obj = MovieRating.objects.get(name=body['movie_rating'])
            else:
                movie_rating_obj = MovieRating.objects.create(name=body['movie_rating'])

            movie_obj.poster_img             = body['poster_img']
            movie_obj.name                   = body['name']
            movie_obj.star_rating            = body['star_rating']
            movie_obj.openning_date          = body['openning_date']
            movie_obj.number_of_viewers      = body['number_of_viewers']
            movie_obj.country_of_manufacture = body['country_of_manufacture']
            movie_obj.genre_id               = genre_obj.genre_no
            movie_obj.movie_rating_id        = movie_rating_obj.movie_rating_no
            movie_obj.running_time           = body['running_time']
            movie_obj.summary                = body['summary']
            movie_obj.save()

            # delete original many to many toble
            for movie_actor_obj in list(MovieActor.objects.filter(movie_id=movie_no)):
                movie_actor_obj.delete()

            # actors & movies_actors table
            for actor in body['actors']:

                if actor in list(Actor.objects.values_list('name', flat=True)):
                    actor_obj = Actor.objects.get(name=actor)
                    MovieActor.objects.create(
                        movie_id = movie_no,
                        actor_id = actor_obj.actor_no
                    )

                else:
                    actor_obj = Actor.objects.create(name=actor)
                    MovieActor.objects.create(
                        movie_id = movie_no,
                        actor_id = actor_obj.actor_no
                    )

            # delete original many to many toble
            for movie_director_obj in MovieDirector.objects.filter(movie_id=movie_no):
                movie_director_obj.delete()

            # directors & movies_directors table
            for director in body['directors']:

                if director in list(Director.objects.values_list('name', flat=True)):
                    director_obj = Director.objects.get(name=director)

                    MovieDirector.objects.create(
                        movie_id    = movie_no,
                        director_id = director_obj.director_no
                    )

                else:
                    director_obj = Director.objects.create(name=director)

                    MovieDirector.objects.create(
                        movie_id    = movie_no,
                        director_id = director_obj.director_no
                    )

            return JsonResponse({'message':'Success PUT Method'}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'message':'It is a movie that does not exist.'}, status=400)

        except Exception as e:
            return JsonResponse({'message':f'{e}'}, status=400)

    def delete(self, request, movie_no):
        try:

            movie_obj = Movie.objects.get(movie_no=movie_no)
            movie_obj.delete()

            return JsonResponse({'message':'Success DELETE Method'}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'message':'It is a movie that does not exist.'}, status=400)

        except Exception as e:
            return JsonResponse({'message':f'{e}'}, status=400)
