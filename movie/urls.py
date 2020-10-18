from django.urls import path
from .views import (
    AllMovieView,
    DetailMovieView
)

urlpatterns = [
    path('', AllMovieView.as_view()),
    path('/<int:movie_no>', DetailMovieView.as_view()),
]
