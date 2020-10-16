# Generated by Django 3.0.7 on 2020-10-16 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'actors',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_no', models.AutoField(primary_key=True, serialize=False)),
                ('poster_img', models.URLField(max_length=500)),
                ('name', models.CharField(max_length=50)),
                ('openning_date', models.DateTimeField(auto_now_add=True)),
                ('grade', models.DecimalField(decimal_places=2, max_digits=4)),
                ('running_time', models.IntegerField()),
                ('desc_text', models.TextField(max_length=2000)),
                ('number_of_viewers', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'types',
            },
        ),
        migrations.CreateModel(
            name='MovieType',
            fields=[
                ('movie_type_no', models.AutoField(primary_key=True, serialize=False)),
                ('movie_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Movie')),
                ('type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Type')),
            ],
            options={
                'db_table': 'movies_types',
            },
        ),
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('movie_actor_no', models.AutoField(primary_key=True, serialize=False)),
                ('actor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Actor')),
                ('movie_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Movie')),
            ],
            options={
                'db_table': 'movies_actors',
            },
        ),
    ]