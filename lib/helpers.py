from models.hotel import Hotel
from models.customer import Customer
from models.review import Review

def initialize_data():
    Hotel.create_table()
    Hotel.get_all()

    Hotel.create_table()
    Customer.get_all()

    Review.create_table()
    Review.get_all()

def exit_program():
    print("Goodbye!")
    exit()

def interact_with_hotels_data():
    while True:
        hotels_menu()
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            get_all_hotels()
        elif choice == "2":
            get_hotel_by_id()
        elif choice == "3":
            create_hotel()
        elif choice == "4":
            update_hotel()
        elif choice == "5":
            delete_hotel()
        elif choice == "6":
            get_reviews_for_hotel()
        else:
            print("Invalid choice! Please try again!")

def get_all_hotels():
    if len(Hotel.all) == 0:
        print("There are no hotels.")
    else:
        for hotel in Hotel.all:
            print(hotel)

    input("-- Enter any key to continue... --\n")

def get_hotel_by_id():
    id = input("Enter a value for the ID for the hotel that you want to retrieve: ")
    
    hotel = Hotel.find_by_id(id)

    if hotel:
        print(hotel)
    else:
        print(f"Error: Hotel # {id} Not Found!")

    input("\n-- Enter any key to continue... --\n")

def create_hotel():
    name = input("Enter the name for your new hotel: ")
    
    try:
        new_hotel = Hotel.create(name)
        print("New hotel successfully created! Here's the info for your new hotel:\n")
        print(new_hotel)
    except ValueError as ve:
        print(ve)
    
    input("\n-- Enter any key to continue... --\n")

def update_hotel():
    id = input("Enter a value for the ID for the hotel that you want to update: ")
    
    hotel = Hotel.find_by_id(id)

    if hotel:
        updated_name = input("Enter the name that you want to update for the hotel: ")
        
        try:
            hotel.name = updated_name
            hotel.update()
            print(f"Hotel # {id} was successfully updated! Here's the information for the updated hotel:\n")
            print(hotel)
        except ValueError as ve:
            print(ve)
    else:
        print(f"Error: Hotel # {id} Not Found!")

    input("\n-- Enter any key to continue... --\n")

def delete_hotel():
    id = input("Enter a value for the ID for the hotel that you want to delete: ")
    
    hotel = Hotel.find_by_id(id)

    if hotel:
        for review in hotel.reviews():
            review.delete()

        hotel.delete()
        print(f"Hotel # {id} and its reviews were successfully deleted!")
    else:
        print(f"Error: Hotel # {id} Not Found!")

    input("\n-- Enter any key to continue... --\n")

def get_reviews_for_hotel():
    id = input("Enter a value for the ID for the hotel that you want to retrieve reviews for: ")
    
    hotel = Hotel.find_by_id(id)

    if hotel:
        if len(hotel.reviews()) == 0:
            print(f"Hotel # {hotel.id} has no reviews.")
        else:
            for review in hotel.reviews():
                print(review)
    else:
        print(f"Error: Hotel # {id} Not Found!")

    input("\n-- Enter any key to continue... --\n")

def interact_with_reviews_data():
    while True:
        reviews_menu()
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            print("Retrieving reviews data...")
            input("-- Enter any key to continue... --\n")
        else:
            print("Invalid choice! Please try again!")

def hotels_menu():
    print("Please select an option:")
    print("0. Return to the previous menu")
    print("1. Retrieve all hotels")
    print("2. Retrieve hotel by ID")
    print("3. Create new hotel")
    print("4. Update an existing hotel")
    print("5. Delete an existing hotel")
    print("6. Retrieve reviews for a hotel")

def reviews_menu():
    print("Please select an option:")
    print("0. Return to the previous menu")
    print("1. Retrieve all reviews")