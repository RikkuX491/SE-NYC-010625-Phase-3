DROP TABLE IF EXISTS restaurants;
DROP TABLE IF EXISTS pizzas;

CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    michelin_stars INTEGER
);

CREATE TABLE IF NOT EXISTS pizzas (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    restaurant_id INTEGER
);

.schema