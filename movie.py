from typing import List

import csv


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2

    def __init__(self, title: str, year: int, genre: List[str], price_code):
        # Initialize a new movie.
        self._title = title
        self._year = year
        self._genre = genre
        self._price_code = price_code

    def get_title(self):
        # get the title
        return self._title

    def get_year(self):
        # get the year
        return self._year

    def get_genre(self):
        # get the genre
        return self._genre

    def is_genre(self, genre: str):
        # check if the genre is the same
        return genre in self._genre

    def get_price_code(self):
        # get the price code
        return self._price_code

    def __str__(self):
        return self._title


class MovieCatalog:
    data_file = 'movie.csv'

    def __init__(self):
        self.movie_list = {}
        with open(self.data_file) as file:
            reader = csv.DictReader(file)
        for movie in reader:
            self.movie_list[movie["title"]] = {
                "#id": movie["#id"],
                "year": movie["year"],
                "genre": [genre for genre in movie["genres"].split("|")]
            }

    def get_movie(self, title):
        movie = self.movie_list[title]
        return Movie(title, movie["year"], movie["genre"])
