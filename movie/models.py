from django.db import models

# movies table
class Movie(models.Model):
    movie_no          = models.AutoField(primary_key=True) # PK
    poster_img        = models.URLField(max_length=500) # 포스터 사진
    name              = models.CharField(max_length=50) # 이름(제목)
    star_rating       = models.DecimalField(max_digits=3, decimal_places=1, default=00.0) # 평점
    openning_date     = models.DateTimeField(auto_now_add=True) # 개봉일
    number_of_viewers = models.IntegerField(default=0, null=True) # 누적 관객수
    running_time      = models.IntegerField() # 러닝 타임
    summary           = models.TextField(max_length=2000) # 줄거리
    country           = models.CharField(max_length=30) # 제작 국가
    rateing           = models.CharField(max_length=30) # 영화 등급

    class Meta:
        db_table='movies'

# types table
class Type(models.Model):
    type_no = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=50)

    class Meta:
        db_table='types'

# movies_types table(Many to Many)
class MovieType(models.Model):
    movie_type_no = models.AutoField(primary_key=True)
    movie_id      = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    type_id       = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table='movies_types'

# actor table
class Actor(models.Model):
    actor_no = models.AutoField(primary_key=True)
    name     = models.CharField(max_length=50)

    class Meta:
        db_table='actors'

# movies_actors table(Many to Many)
class MovieActor(models.Model):
    movie_actor_no = models.AutoField(primary_key=True)
    movie_id       = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    actor_id       = models.ForeignKey(Actor, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table='movies_actors'
