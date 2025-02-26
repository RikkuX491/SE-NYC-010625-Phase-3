.mode column

DELETE FROM restaurants;
DELETE FROM pizzas;

INSERT INTO restaurants (name, michelin_stars) VALUES ("Una Pizza Napoletana", 2);
INSERT INTO restaurants (name, michelin_stars) VALUES ("Stellina Pizzeria", 1);

INSERT INTO pizzas (name, price, restaurant_id) VALUES ("Pepperoni Pizza", 22.99, 1);
INSERT INTO pizzas (name, price, restaurant_id) VALUES ("Taco Pizza", 25.99, 1);
INSERT INTO pizzas (name, price, restaurant_id) VALUES ("Eggplant Parmigiana Pizza", 20.99, 2);

-- Display information about the restaurants from the restaurants table
SELECT * FROM restaurants;

-- Display information about the pizzas from the pizzas table
SELECT * FROM pizzas;

-- Display the 1-to-Many information about the pizzas that belong to the restaurant with id of 1. We assume that there is a restaurants table already created.
SELECT * FROM pizzas WHERE restaurant_id = 1;

-- We can also write the statement like this to get the data for the pizzas that belong to the restaurant with the id of 1. GROUP BY is used remove duplicate data from SELECT.
-- This requires both the restaurants table and pizzas table to exist and gives us the most accurate result.
SELECT pizzas.* FROM pizzas
INNER JOIN restaurants
ON restaurants.id = pizzas.restaurant_id
WHERE pizzas.restaurant_id = 1
GROUP BY pizzas.id;

-- Display the data for the restaurant that a pizza belongs to (this is the belongs to side of the 1-to-Many relationship). In this case, the pizza belongs to the restaurant with id of 1. We assume that there is a pizzas table already created, such that pizzas belong to a restaurant, and a restaurant has many pizzas.
SELECT * FROM restaurants WHERE id = 1;

-- We can also write the statement like this to get the data for a restaurant that a pizza belongs to (in this case, the pizza belongs to the restaurant with id of 1), using INNER JOIN (LIMIT 1 is used only display the 1st result from SELECT).
-- This requires both the restaurants table and pizzas table to exist and gives us the most accurate result.
SELECT restaurants.* FROM restaurants
INNER JOIN pizzas
ON restaurants.id = pizzas.restaurant_id
WHERE pizzas.restaurant_id = 1
LIMIT 1;