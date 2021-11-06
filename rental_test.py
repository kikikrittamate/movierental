import unittest
from customer import Customer
from rental import Rental, PriceCode
from movie import Movie


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("A Tenant", 2020, ["Action", "Sci-Fi"], PriceCode.new_release)
		self.regular_movie = Movie("La La Land", 2016, ["Comedy", "Drama", "Romance"], PriceCode.regular)
		self.children_movie = Movie("Weathering With You", 2020, ["Animation", "Drama", "Children"], PriceCode.children)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("La La Land", 2016, ["Comedy", "Drama", "Romance"], PriceCode.regular)
		self.assertEqual("La La Land", m.get_title())
		self.assertEqual(PriceCode.regular, m.get_price_code())

	def test_rental_price(self):
		# test for new movie
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		# test for regular movie
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_price(), 6.5)
		# test for children movie
		rental = Rental(self.children_movie, 1)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.children_movie, 5)
		self.assertEqual(rental.get_price(), 4.5)

	def test_rental_points(self):
		# test for new movie
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_renter_points(), 1)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_renter_points(), 5)
		# test for regular movie
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_renter_points(), 1)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_renter_points(), 1)
		# test for children movie
		rental = Rental(self.children_movie, 1)
		self.assertEqual(rental.get_renter_points(), 1)
		rental = Rental(self.children_movie, 5)
		self.assertEqual(rental.get_renter_points(), 1)

