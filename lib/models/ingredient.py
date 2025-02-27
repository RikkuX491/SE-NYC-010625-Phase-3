from models.__init__ import EXAMPLE_CONN, EXAMPLE_CURSOR

# An ingredient belongs to a pizza (Opposite side of the 1-to-Many relationship)
class Ingredient:

    all = []

    def __init__(self, name, pizza_id):
        self.name = name
        self.pizza_id = pizza_id
        self.id = None

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY,
                name TEXT,
                pizza_id INTEGER
            )
        '''

        EXAMPLE_CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS ingredients
        '''

        EXAMPLE_CURSOR.execute(sql)

    def save(self):
        sql = '''
            INSERT INTO ingredients (name, pizza_id)
            VALUES (?, ?)
        '''

        EXAMPLE_CURSOR.execute(sql, (self.name, self.pizza_id))
        EXAMPLE_CONN.commit()

        self.id = EXAMPLE_CURSOR.lastrowid

        Ingredient.all.append(self)

    @classmethod
    def create(cls, name, pizza_id):
        new_ingredient = cls(name, pizza_id)
        new_ingredient.save()
        return new_ingredient
    
    @classmethod
    def instance_from_db(cls, row):
        new_ingredient = cls(row[1], row[2])
        new_ingredient.id = row[0]
        return new_ingredient
    
    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM ingredients WHERE id = ?
        '''

        row = EXAMPLE_CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None
    
    # Here's the relationship method to get the Pizza instance for the opposite side of the 1-to-Many Relationship (An Ingredient belongs to a Pizza)
    def pizza(self):
        from models.pizza import Pizza

        sql = '''
            SELECT * FROM pizzas
            WHERE id = ?
        '''

        row = EXAMPLE_CURSOR.execute(sql, (self.pizza_id,)).fetchone()
        
        if row:
            return Pizza.instance_from_db(row)
        else:
            return None
    
    # Optional - A __repr__() method to make our instances more readable
    def __repr__(self):
        return f"<Ingredient # {self.id} - Name: {self.name}, Pizza ID: {self.pizza_id}>"