from models.__init__ import EXAMPLE_CONN, EXAMPLE_CURSOR

# 1 Pizza has many Ingredients (1-to-Many relationship)
class Pizza:

    all = []
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = None

    @property
    def name_getter(self):
        return self._name
    
    @name_getter.setter
    def name(self, value):
        if not (type(value) == str):
            raise TypeError("Name must be a string!")
        elif len(value) < 3:
            raise ValueError("Pizza names must be at least 3 characters long!")
        else:
            self._name = value

    @property
    def price_getter(self):
        return self._price
    
    @price_getter.setter
    def price(self, value):
        if not (type(value) == float):
            raise TypeError("Price must be a floating point number!")
        elif value <= 0:
            raise ValueError("Price must be greater than 0!")
        else:
            self._price = value

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS pizzas (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL
            )
        '''

        EXAMPLE_CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS pizzas
        '''

        EXAMPLE_CURSOR.execute(sql)

    def save(self):
        sql = '''
            INSERT INTO pizzas (name, price) VALUES (?, ?)
        '''

        EXAMPLE_CURSOR.execute(sql, (self.name, self.price))
        EXAMPLE_CONN.commit()

        self.id = EXAMPLE_CURSOR.lastrowid

        Pizza.all.append(self)

    @classmethod
    def create(cls, name, price):
        new_pizza = cls(name, price)
        new_pizza.save()
        return new_pizza
    
    @classmethod
    def instance_from_db(cls, row):
        new_pizza = cls(row[1], row[2])
        new_pizza.id = row[0]
        return new_pizza
    
    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM pizzas
        '''

        rows = EXAMPLE_CURSOR.execute(sql).fetchall()
        
        cls.all = [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM pizzas WHERE id = ?
        '''

        row = EXAMPLE_CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
        
    def update(self):
        sql = '''
            UPDATE pizzas
            SET name = ?, price = ?
            WHERE id = ?
        '''

        EXAMPLE_CURSOR.execute(sql, (self.name, self.price, self.id))
        EXAMPLE_CONN.commit()

    def delete(self):
        sql = '''
            DELETE FROM pizzas
            WHERE id = ?
        '''

        EXAMPLE_CURSOR.execute(sql, (self.id,))
        EXAMPLE_CONN.commit()

        Pizza.all = [pizza for pizza in Pizza.all if pizza.id != self.id]

    # Here's the relationship method to get the Ingredient instances for the 1-to-Many Relationship (1 Pizza has many Ingredients)
    def ingredients(self):
        from models.ingredient import Ingredient

        sql = '''
            SELECT * FROM ingredients
            WHERE pizza_id = ?
        '''

        rows = EXAMPLE_CURSOR.execute(sql, (self.id,)).fetchall()
        return [Ingredient.instance_from_db(row) for row in rows]
    
    # Optional - A __repr__() method to make our instances more readable
    def __repr__(self):
        return f"<Pizza # {self.id} - Name: {self.name}, Price: {self.price}>"