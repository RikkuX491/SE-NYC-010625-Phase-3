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