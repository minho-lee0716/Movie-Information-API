from django.db import models

# movies table
class Movie(models.Model):
    movie_no          = models.AutoField(primary_key=True)
    poster_img        = models.URLField(max_length=500,)
    name              = models.CharField(max_length=50,)
    openning_date     = models.DateTimeField(auto_now_add=True)
    grade             = models.DecimalField(max_digits=4, decimal_places=2)
    running_time      = models.IntegerField()
    introduction      = models.TextField(max_length=2000)
    number_of_viewers = models.IntegerField(default=0)

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
