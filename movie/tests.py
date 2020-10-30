'''
from django.test import TestCase

# Create your tests here.
'''

from django.test import (
    TestCase,
    Client
)

from .models import (
    Movie,
    Genre,
    MovieRating,
    Actor,
    Director,
    MovieActor,
    MovieDirector
)

import json

class AllMovieViewTest(TestCase):

    def test_get(self):

        client = Client()
        response = client.get('/movie')

        expected_json_data = {
            "data": [
                {
                    "movie_no": 1,
                    "poster_img": "https://search1.daumcdn.net/thumb/C146x211.q70/?fname=http%3A%2F%2Fcfile16.uf.daum.net%2FC110x160%2F2776AD4E53CC5FDE262010",
                    "name": "명량",
                    "star_rating": 7.8,
                    "openning_date": "2020-10-19",
                    "number_of_viewers": 17615686
                },
                {
                    "movie_no": 2,
                    "poster_img": "https://search1.daumcdn.net/thumb/C146x211.q70/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F4e00e81f2b6f4d2eb65b3387240cc3c01547608409838",
                    "name": "극한직업",
                    "star_rating": 7.4,
                    "openning_date": "2020-10-19",
                    "number_of_viewers": 16266338
                },
                {
                    "movie_no": 3,
                    "poster_img": "https://search1.daumcdn.net/thumb/C146x211.q70/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fff9d430c0d2df2a1c659ccba8b621ad2251f6f02",
                    "name": "신과함께-죄와 벌",
                    "star_rating": 7.0,
                    "openning_date": "2020-10-19",
                    "number_of_viewers": 14411782
                },
                {
                    "movie_no": 4,
                    "poster_img": "https://search1.daumcdn.net/thumb/C146x211.q70/?fname=http%3A%2F%2Fcfile76.uf.daum.net%2FC110x160%2F2502AF49546B09E61FB5F1",
                    "name": "국제시장",
                    "star_rating": 7.1,
                    "openning_date": "2020-10-19",
                    "number_of_viewers": 14263980
                },
                {
                    "movie_no": 5,
                    "poster_img": "https://search1.daumcdn.net/thumb/C146x211.q70/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F5574fb2c20c844629aa9ad1d6043ee851555464908641",
                    "name": "어벤져스: 엔드게임",
                    "star_rating": 7.8,
                    "openning_date": "2020-10-19",
                    "number_of_viewers": 13977602
                },
                {
                    "movie_no": 6,
                    "poster_img": "https://search1.daumcdn.net/thumb/C146x211.q70/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F5afd212b68e34e61a964d969dd898e2f1574298873981",
                    "name": "겨울왕국2",
                    "star_rating": 7.3,
                    "openning_date": "2019-11-21",
                    "number_of_viewers": 14263980
                }
            ]
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_json_data)


    def test_get_url_query(self):
        client = Client()
        response = client.get('/movie/5')

        expected_json_data = {
            "data": {
                "movie_no": 5,
                "poster_img": "https://search1.daumcdn.net/thumb/C146x211.q70/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F5574fb2c20c844629aa9ad1d6043ee851555464908641",
                "name": "어벤져스: 엔드게임",
                "star_rating": 7.8,
                "openning_date": "2020-10-19",
                "number_of_viewers": 13977602,
                "country_of_manufacture": "미국",
                "genre": "액션",
                "movie_rating": "12세이상관람가",
                "running_time": 181,
                "directors": [
                    "안소니루소",
                    "조루소"
                ],
                "actors": [
                    "로버트다우니주니어",
                    "크리스에반스",
                    "마크러팔로",
                    "스칼렛요한슨"
                ],
                "summary": "인피니티 워 이후 절반만 살아남은 지구 마지막 희망이 된 어벤져스 먼저 "
            }
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_json_data)
