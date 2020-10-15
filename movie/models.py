from django.db import models

class Movie(models.Model):
    movie_no = models.AutoField(primary_key=True)
    poster_img = models.URLField(max_length=500, null=False)
    name = models.CharField(max_length=50, null=False)
    openning_date = models.DateTimeField(auto_now_add=True)
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    running_time = models.IntegerField(null=False)
    desc_text = models.TextField(max_length=2000)
    number_of_viewers = models.IntegerField(default=0)

    class Meta:
        db_table='movies'
