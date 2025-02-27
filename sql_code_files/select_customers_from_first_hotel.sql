.mode column

-- Deliverable # 7 solution code
SELECT customers.* from customers
INNER JOIN reviews
ON customers.id = reviews.customer_id
INNER JOIN hotels
ON hotels.id = reviews.hotel_id
WHERE hotels.id = 1
GROUP BY customers.id;