from django.db import models

# movies table
class Movie(models.Model):
    movie_no               = models.AutoField(primary_key=True) # PK
    poster_img             = models.URLField(max_length=500, default='') # 포스터 사진
    name                   = models.CharField(max_length=50, default='') # 이름(제목)
    star_rating            = models.DecimalField(max_digits=3, decimal_places=1, default=00.0) # 평점
    openning_date          = models.DateField(auto_now_add=True) # 개봉일
    number_of_viewers      = models.IntegerField(default=0) # 누적 관객수
    country_of_manufacture = models.CharField(max_length=30, default='') # 제작 국가
    genre                  = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True) # foreignkey to Genre table
    movie_rating           = models.ForeignKey('MovieRating', on_delete=models.SET_NULL, null=True) # 영화 등급
    running_time           = models.IntegerField(default=0) # 러닝 타임(분 단위)
    summary                = models.CharField(max_length=300, default='') # 줄거리

    class Meta:
        db_table='movies'

# genres table
class Genre(models.Model):
    genre_no = models.AutoField(primary_key=True) # PK
    name     = models.CharField(max_length=30) # 장르 이름

    class Meta:
        db_table='genres'

class MovieRating(models.Model):
    movie_rating_no = models.AutoField(primary_key=True) # PK
    name            = models.CharField(max_length=30) # 영화 등급

    class Meta:
        db_table='movie_ratings'

# actors table
class Actor(models.Model):
    actor_no = models.AutoField(primary_key=True) # PK
    name     = models.CharField(max_length=30) # 배우 이름
    to_Movie = models.ManyToManyField(Movie, through='MovieActor') # many to many field

    class Meta:
        db_table='actors'

# directors table
class Director(models.Model):
    director_no = models.AutoField(primary_key=True) # PK
    name        = models.CharField(max_length=30) # 감독 이름
    to_movie    = models.ManyToManyField(Movie, through='MovieDirector') # many to many field

    class Meta:
        db_table='directors'

# movies_actors table
class MovieActor(models.Model):
    movie_actor_no = models.AutoField(primary_key=True)
    movie          = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    actor          = models.ForeignKey(Actor, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table='movies_actors'

# movies_directors table
class MovieDirector(models.Model):
    movie_director_no = models.AutoField(primary_key=True)
    movie             = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    director          = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table='movies_directors'
