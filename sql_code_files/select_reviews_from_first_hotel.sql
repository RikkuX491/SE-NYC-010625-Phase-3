.mode column

-- Deliverable # 6 solution code
SELECT reviews.* FROM reviews
INNER JOIN hotels
ON hotels.id = reviews.hotel_id
WHERE reviews.hotel_id = 1
GROUP BY reviews.id;