#!/usr/bin/env python3
import ipdb;

from models.__init__ import CONN, CURSOR, EXAMPLE_CONN, EXAMPLE_CURSOR
from models.hotel import Hotel
from models.customer import Customer
from models.review import Review

# Our example model from class today
from models.pizza import Pizza
from models.ingredient import Ingredient

if __name__ == '__main__':
    # don't remove this line, it's for debugging!
    ipdb.set_trace()