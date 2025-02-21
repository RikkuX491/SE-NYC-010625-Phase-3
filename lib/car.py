class Car:

    # Deliverable # 3 solution code
    all = []
    
    def __init__(self, make, model, year, horn_volume=1):
        self.make = make
        self.model = model
        self.year = year
        self.horn_volume = horn_volume

        if len(Car.all) == 0:
            self.id = 1
        else:
            last_car = Car.all[-1]
            self.id = last_car.id + 1
        
        Car.all.append(self)

    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, value):
        if not (type(value) == str):
            raise TypeError("Make must be a string!")
        elif len(value) < 3:
            raise ValueError("Make must be at least 3 characters long!")
        else:
            self._make = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if not (type(value) == int):
            raise TypeError("Year must be an integer!")
        elif not (1900 <= value <= 2024):
            raise ValueError("Year must be between 1900 and 2024!")
        else:
            self._year = value

    @property
    def horn_volume(self):
        return self._horn_volume
    
    @horn_volume.setter
    def horn_volume(self, value):
        if not (type(value) == int):
            raise TypeError("Horn Volume must be an integer!")
        elif not (1 <= value <= 10):
            raise ValueError("Horn Volume must be between 1 and 10!")
        else:
            self._horn_volume = value

    def honk_horn(self):
        print(f"BEEP BEEP{'!' * self.horn_volume}")

    # Deliverable # 2 solution code
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        if hasattr(self, 'model') or not (type(value) == str):
            raise Exception
        
        self._model = value

    # Deliverable # 4 solution code
    @classmethod
    def average_year(cls):
        # This if statement is useful, since if the list is empty, len(year_list) will be 0, and we'll get a ZeroDivisionError if we divide by 0
        if len(cls.all) == 0:
            return 0
        else:
            year_list = [car.year for car in cls.all]
            return sum(year_list) / len(year_list)
    
    # Here's a class method that returns a list of cars that have a particular make
    @classmethod
    def cars_with_make(cls, make):
        # print(make)
        return [car for car in cls.all if car.make == make]
    
    def __repr__(self):
        return f"<Car # {self.id} - Make: {self.make}, Mode: {self.model}, Year: {self.year}, Horn Volume: {self.horn_volume}>"