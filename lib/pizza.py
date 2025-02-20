import ipdb

class Pizza:

    def __init__(self, name, ingredients, price=25.99, size=2):
        # print(self)
        # print("New pizza created!")
        # print(name)
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.size = size

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if type(value) == str:
            self._name = value
        else:
            raise TypeError
        
    name = property(get_name, set_name)

    @property
    def price(self):
        # print('Getter for price...')
        return self._price
    
    @price.setter
    def price(self, value):
        # print("Setter for price...")
        if not (type(value) in [int, float]):
            raise TypeError
        elif value < 20:
            raise ValueError
        
        self._price = value

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not hasattr(self, 'size'):
            # print(hasattr(self, 'size'))
            # print('creating size...')
            self._size = value
        else:
            # print("can't change size")
            raise Exception("Can't change size of pizza!")
        
    def __repr__(self):
        return f"<Pizza - Name: {self.name}, Ingredients: {self.ingredients}, Price: {self.price}, Size: {self.size}>"

pepperoni_pizza = Pizza("Pepperoni Pizza", "Pepperoni, cheese", 24.99)
supreme_pizza = Pizza("Supreme Pizza", "Sausage, peppers, onions, cheese")

# Accessing the value vs using getattr to access the value of an instance's attribute
pizza_name = pepperoni_pizza.name
print(pizza_name)

pizza_name = getattr(pepperoni_pizza, 'name')
print(pizza_name)

attr_name = 'name'
new_value = 'Pepperoni Lasagna'

setattr(pepperoni_pizza, attr_name, new_value)

ipdb.set_trace()