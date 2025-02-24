class Hotel:
    
    def __init__(self, name):
        self.name = name

    @property
    def name_getter(self):
        return self._name
    
    @name_getter.setter
    def name(self, name_value):
        if (type(name_value) == str) and (5 <= len(name_value) <= 20):
            self._name = name_value

    def reviews(self):
        return [review for review in Review.all if review.hotel is self]
    
    def customers(self):
        return list(set([review.customer for review in self.reviews()]))
    
    def review_texts(self):
        if len(self.reviews()) == 0:
            return None
        else:
            return [review.text for review in self.reviews()]
        
    def average_rating(self):
        if len(self.reviews()) == 0:
            return None
        else:
            rating_list = [review.rating for review in self.reviews()]
            return sum(rating_list) / len(rating_list)
        
    def customers_more_than_three_reviews(self):
        customer_list = [customer for customer in self.customers() if self.has_more_than_3_reviews(customer)]

        if len(customer_list) == 0:
            return None
        else:
            return customer_list
    
    def has_more_than_3_reviews(self, customer):
        review_list = [review for review in customer.reviews() if review.hotel is self]
        
        if len(review_list) > 3:
            return True
        else:
            return False

class Customer:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name_getter(self):
        return self._first_name
    
    @first_name_getter.setter
    def first_name(self, first_name_value):
        if (not hasattr(self, 'first_name')) and (type(first_name_value) == str) and (len(first_name_value) > 0):
            self._first_name = first_name_value

    @property
    def last_name_getter(self):
        return self._last_name
    
    @last_name_getter.setter
    def last_name(self, last_name_value):
        if (not hasattr(self, 'last_name')) and (type(last_name_value) == str) and (len(last_name_value) > 0):
            self._last_name = last_name_value

    def reviews(self):
        return [review for review in Review.all if review.customer is self]
    
    def hotels(self):
        return list(set([review.hotel for review in self.reviews()]))
    
    def submit_review(self, hotel, rating, text):
        return Review(hotel, self, rating, text)
    
    def hotel_names(self):
        return [hotel.name for hotel in self.hotels()]
    
class Review:

    all = []
    
    def __init__(self, hotel, customer, rating, text):
        self.hotel = hotel
        self.customer = customer
        self.rating = rating
        self.text = text
        Review.all.append(self)

    @property
    def rating_getter(self):
        return self._rating
    
    @rating_getter.setter
    def rating(self, rating_value):
        if (not hasattr(self, 'rating')) and (type(rating_value) == int) and (1 <= rating_value <= 5):
            self._rating = rating_value

    @property
    def text_getter(self):
        return self._text
    
    @text_getter.setter
    def text(self, text_value):
        if (not hasattr(self, 'text')) and (type(text_value) == str) and (3 <= len(text_value) <= 40):
            self._text = text_value

    @property
    def hotel_getter(self):
        return self._hotel
    
    @hotel_getter.setter
    def hotel(self, hotel_value):
        if isinstance(hotel_value, Hotel):
            self._hotel = hotel_value

    @property
    def customer_getter(self):
        return self._customer
    
    @customer_getter.setter
    def customer(self, customer_value):
        if isinstance(customer_value, Customer):
            self._customer = customer_value