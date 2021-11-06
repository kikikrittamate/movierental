class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2

    def __init__(self, title, year, genre, price_code):
        # Initialize a new movie.
        self.title = title
        self.year = year
        self.genre = genre
        self.price_code = price_code

    def get_title(self):
        # get the title
        return self.title

    def get_year(self):
        # get the year
        return self.year

    def get_genre(self):
        # get the genre
        return self.genre

    def get_price_code(self):
        # get the price code
        return self.price_code

    def __str__(self):
        return self.title
