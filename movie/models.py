from django.db import models

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)

    class Meta:
        db_table='movies'
