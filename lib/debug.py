#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Hotel
from classes.many_to_many import Customer
from classes.many_to_many import Review

if __name__ == '__main__':
    # don't remove this line, it's for debugging!

    # Hotels
    marriott = Hotel("Marriott")
    the_chanler_at_cliff_walk = Hotel("Chanler Hotel")

    # Customers
    alice_baker = Customer("Alice", "Baker")
    bob_carris = Customer("Bob", "Carris")

    # Reviews
    review_1 = Review(marriott, alice_baker, 4, "Pretty awesome amenities here!")
    review_2 = Review(the_chanler_at_cliff_walk, alice_baker, 5, "Best hotel ever!")
    review_3 = Review(marriott, alice_baker, 3, "Not as great as my first visit.")
    review_4 = Review(marriott, bob_carris, 5, "Amazing!")

    ipdb.set_trace()