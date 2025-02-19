import ipdb

# Sequences - list, tuple, str

# A list of two numbers
numbers_list = [7, 14]

# A tuple that has one number
numbers_tuple = (8,)

# A tuple that has a string and a boolean
items = ('pizza', True)

# A list of duplicate numbers
duplicate_numbers_list = [2, 2, 3, 3, 4, 4]

# A set that removes the duplicate items from the list
numbers_set = set(duplicate_numbers_list)

# A list that contains the numbers without the duplicates
numbers_list_without_duplicates = list(numbers_set)

# A string
phrase = 'hello flatiron'

# A string of duplicate characters
fruit = "apple"

# A set that removes the duplicate characters from the "apple" string
set_of_chars = set(fruit)

# Taking the characters from the set and creating a new string that contains these characters with the duplicates having been removed
new_string = ""
for char in set_of_chars:
    new_string += char

print(f"My favorite phrase is {phrase}")

def combine_sequences(seq1, seq2):
    pass

def sequence_n_times(seq, n):
    pass

def average(seq):
    pass

def append_n_times(input_list, element, n):
    pass

foods = [
    {
        "name": "Flatburger",
        "price": 9.50
    },
    {
        "name": "French Fries",
        "price": 1.25
    },
    {
        "name": "Burrito",
        "price": 7.25
    }
]

# Example code that returns a filtered list of the prices that are greater than 3
filtered_prices_list = [food['price'] for food in foods if food['price'] > 3]

animals = [
    {
        "name": "Fido",
        "animal_type": "Dog"
    },
    {
        "name": "Kitty",
        "animal_type": "Cat"
    },
    {
        "name": "Fluffy",
        "animal_type": "Guinea Pig"
    }
]

ipdb.set_trace()