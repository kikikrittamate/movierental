from rental import Rental
from movie import Movie
import logging


class Customer:
    """
       A customer who rents movies.
       The customer object holds information about the
       movies rented for the current billing period,
       and can print a statement of his rentals.
    """
    def __init__(self, name: str):
        """ Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        if rental not in self.rentals:
            self.rentals.append(rental)
    
    def get_name(self):
        return self.name
    
    def statement(self):
        """
            Print all the rentals in current period, 
            along with total charges and reward points.
            Returns:
                the statement as a String
        """
        total_amount = 0 # total charges
        frequent_renter_points = 0
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"
        
        for rental in self.rentals:
            # award renter points
            frequent_renter_points += rental.get_frequent_renter_points
            #  add detail line to statement
            statement += fmt.format(rental.get_movie().get_title(), rental.get_days_rented(), rental.get_amount)
            # and accumulate activity
            total_amount += rental.get_amount

        # footer: summary of charges
        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
                       "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement

    def get_amount(self):
        # compute rental change
        amount = 0
        if self.get_movie().get_price_code() == Movie.REGULAR:
            # Two days for $2, additional days 1.50 each.
            amount = 2.0
            if self.get_days_rented() > 2:
                amount += 1.5 * (self.get_days_rented() - 2)
        elif self.get_movie().get_price_code() == Movie.CHILDREN:
            # Three days for $1.50, additional days 1.50 each.
            amount = 1.5
            if self.get_days_rented() > 3:
                amount += 1.5 * (self.get_days_rented() - 3)
        elif self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            # Straight per day charge
            amount = 3 * self.get_days_rented()
        else:
            log = logging.getLogger()
            log.error(f"Movie {self.get_movie()} has unrecognized priceCode {self.get_movie().get_price_code()}")
        return amount

    def get_frequent_renter_points(self):
        # award renter points
        frequent_renter_points = 0
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            frequent_renter_points += self.get_days_rented()
        else:
            frequent_renter_points += 1
        return frequent_renter_points


if __name__ == "__main__":
    customer = Customer("Edward Snowden")
    print(customer.statement())
    movie = Movie("Hacker Noon", Movie.REGULAR)
    customer.add_rental(Rental(movie, 2))
    movie = Movie("CitizenFour", Movie.NEW_RELEASE)
    customer.add_rental(Rental(movie, 3))
    print(customer.statement())
