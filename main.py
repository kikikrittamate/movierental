# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental, PriceCode
from customer import Customer


def make_movies():
    catalog = MovieCatalog()
    movies = [
        catalog.get_movie("Mulan"),
        catalog.get_movie("Weathering With You"),
        catalog.get_movie("Deadpool"),
        catalog.get_movie("Steve Jobs"),
        catalog.get_movie("Spectre")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
