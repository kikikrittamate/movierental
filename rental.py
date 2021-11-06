from enum import Enum

from movie import Movie

from datetime import datetime


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for a movie	\
        with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        return self.get_movie().get_price_code().price(self.days_rented)

    def get_renter_points(self):
        return self.get_movie().get_price_code().renter_points(self.days_rented)

    def for_movie(self, movie: Movie):
        current_year = datetime.now().year
        if current_year == movie.get_year():
            return PriceCode.new_release
        if movie.is_genre("Children"):
            return PriceCode.children
        return PriceCode.regular


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""

    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    regular = {"price": lambda days: 2.0 + max((1.5 * (days-2)), 0),
               "frp": lambda days: 1
               }
    children = {"price": lambda days: 1.5 + max((1.5 * (days-3)), 0),
                "frp": lambda days: 1
                }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def renter_points(self, days: int) -> int:
        """Return the the rental points for a given number of days."""
        frp = self.value["frp"]  # the enum member's frp formula
        return frp(days)
