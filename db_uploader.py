import os, django, csv, sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from movie.models import (
    Movie,
    Genre,
    MovieRating,
    Actor,
    Director,
    MovieActor,
    MovieDirector
)

CSV_PATH_PRODUCTS = 'movies.csv'

# movies, genres, movie_ratings
with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)

    for row in data_reader:

        if len(Genre.objects.all()) == 0:
            Genre.objects.create(name=row[6])
            MovieRating.objects.create(name=row[7])
            Movie.objects.create(
                poster_img             = row[0],
                name                   = row[1],
                star_rating            = row[2],
                openning_date          = row[3],
                number_of_viewers      = row[4],
                country_of_manufacture = row[5],
                genre_id               = Genre.objects.get(name=row[6]).genre_no,
                movie_rating_id        = MovieRating.objects.get(name=row[7]).movie_rating_no,
                running_time           = row[8],
                summary                = row[11]
            )

        else:
            genre_list = [genre['name'] for genre in list(Genre.objects.values('name'))]
            movie_rating_list = [movie_rating['name'] for movie_rating in list(MovieRating.objects.values('name'))]

            if row[6] in genre_list:

                if row[7] in movie_rating_list:
                    Movie.objects.create(
                        poster_img             = row[0],
                        name                   = row[1],
                        star_rating            = row[2],
                        openning_date          = row[3],
                        number_of_viewers      = row[4],
                        country_of_manufacture = row[5],
                        genre_id               = Genre.objects.get(name=row[6]).genre_no,
                        movie_rating_id        = MovieRating.objects.get(name=row[7]).movie_rating_no,
                        running_time           = row[8],
                        summary                = row[11]
                    )

                else:
                    MovieRating.objects.create(name=row[7])
                    Movie.objects.create(
                        poster_img             = row[0],
                        name                   = row[1],
                        star_rating            = row[2],
                        openning_date          = row[3],
                        number_of_viewers      = row[4],
                        country_of_manufacture = row[5],
                        genre_id               = Genre.objects.get(name=row[6]).genre_no,
                        movie_rating_id        = MovieRating.objects.get(name=row[7]).movie_rating_no,
                        running_time           = row[8],
                        summary                = row[11]
                    )
            else:
                if row[7] in movie_rating_list:
                    Genre.objects.create(name=row[6])
                    Movie.objects.create(
                        poster_img             = row[0],
                        name                   = row[1],
                        star_rating            = row[2],
                        openning_date          = row[3],
                        number_of_viewers      = row[4],
                        country_of_manufacture = row[5],
                        genre_id               = Genre.objects.get(name=row[6]).genre_no,
                        movie_rating_id        = MovieRating.objects.get(name=row[7]).movie_rating_no,
                        running_time           = row[8],
                        summary                = row[11]
                    )

                else:
                    Genre.objects.create(name=row[6])
                    MovieRating.objects.create(name=row[7])
                    Movie.objects.create(
                        poster_img             = row[0],
                        name                   = row[1],
                        star_rating            = row[2],
                        openning_date          = row[3],
                        number_of_viewers      = row[4],
                        country_of_manufacture = row[5],
                        genre_id               = Genre.objects.get(name=row[6]).genre_no,
                        movie_rating_id        = MovieRating.objects.get(name=row[7]).movie_rating_no,
                        running_time           = row[8],
                        summary                = row[11]
                    )

# actors, movies_actors
with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)

    for row in data_reader:

        if len(Actor.objects.all()) == 0:

            if ',' in row[10]:
                actors = row[10].split(',')

                for actor in actors:
                    Actor.objects.create(name=actor)
                    MovieActor.objects.create(
                        movie_id = Movie.objects.get(name=row[1]).movie_no,
                        actor_id = Actor.objects.get(name=actor).actor_no
                    )
            else:
                Actor.objects.create(name=row[10])
                MovieActor.objects.create(
                    movie_id = Movie.objects.get(name=row[1]).movie_no,
                    actor_id = Actor.objects.get(name=row[10]).actor_no
                )
        else:
            actor_list = [actor['name'] for actor in list(Actor.objects.values('name'))]

            if ',' in row[10]:
                actors = row[10].split(',')

                for actor in actors:

                    if actor in actor_list:
                        MovieActor.objects.create(
                            movie_id = Movie.objects.get(name=row[1]).movie_no,
                            actor_id = Actor.objects.get(name=actor).actor_no
                        )
                    else:
                        Actor.objects.create(name=actor)
                        MovieActor.objects.create(
                            movie_id = Movie.objects.get(name=row[1]).movie_no,
                            actor_id = Actor.objects.get(name=actor).actor_no
                        )
            else:
                if row[10] in actor_list:
                    MovieActor.objects.create(
                        movie_id = Movie.objects.get(name=row[1]).movie_no,
                        actor_id = Actor.objects.get(name=row[10]).actor_no
                    )
                else:
                    Actor.objects.create(name=row[10])
                    MovieActor.objects.create(
                        movie_id = Movie.objects.get(name=row[1]).movie_no,
                        actor_id = Actor.objects.get(name=row[10]).actor_no
                    )

# directors, movies_directors
with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)

    for row in data_reader:

        if len(Director.objects.all()) == 0:

            if ',' in row[9]:
                directors = row[9].split(',')

                for director in directors:
                    Director.objects.create(name=director)
                    MovieDirector.objects.create(
                        movie_id    = Movie.objects.get(name=row[1]).movie_no,
                        director_id = Director.objects.get(name=director).director_no
                    )
            else:
                Director.objects.create(name=row[9])
                MovieDirector.objects.create(
                    movie_id    = Movie.objects.get(name=row[1]).movie_no,
                    director_id = Director.objects.get(name=row[9]).director_no
                )
        else:
            director_list = [director['name'] for director in list(Director.objects.values('name'))]

            if ',' in row[9]:
                directors = row[9].split(',')

                for director in directors:
                    if director in director_list:
                        MovieDirector.objects.create(
                            movie_id    = Movie.objects.get(name=row[1]).movie_no,
                            director_id = Director.objects.get(name=director).director_no
                        )

                    else:
                        Director.objects.create(name=director)
                        MovieDirector.objects.create(
                            movie_id    = Movie.objects.get(name=row[1]).movie_no,
                            director_id = Director.objects.get(name=director).director_no
                        )
            else:

                if row[9] in director_list:
                    MovieDirector.objects.create(
                        movie_id    = Movie.objects.get(name=row[1]).movie_no,
                        director_id = Director.objects.get(name=row[9]).director_no
                    )
                else:

                    Director.objects.create(name=row[9])
                    MovieDirector.objects.create(
                        movie_id    = Movie.objects.get(name=row[1]).movie_no,
                        director_id = Director.objects.get(name=row[9]).director_no
                    )
