import sqlite3

CONN = sqlite3.connect('hotel_reviews.db')
CURSOR = CONN.cursor()

EXAMPLE_CONN = sqlite3.connect('pizzas.db')
EXAMPLE_CURSOR = EXAMPLE_CONN.cursor()