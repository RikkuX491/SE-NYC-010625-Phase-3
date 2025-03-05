from models.page import Page
from models.room import Room

def exit_program():
    print("Goodbye!")
    exit()

def traverse_through_pages():
    # First we'll retrieve the pages from the database and populate the Singly Linked List
    Page.get_all()

    current_page = Page.singly_linked_list.head

    while current_page:
        print(f'Page # {current_page.id}: {current_page.text}')

        decision = input("\nWould you like to read the next page? (Enter 'Yes' to continue reading) ")

        if decision in ['Yes', 'yes', 'y', 'Y']:
            current_page = current_page.next_node
        else:
            input("\nYou've decided to stop reading the book.\n")
            return

    input("\nYou've reached the end of the book! Enter any key to continue...\n")

def traverse_through_rooms():
    # First we'll retrieve the rooms from the database and populate the Doubly Linked List
    Room.get_all()

    current_room = Room.doubly_linked_list.head

    while current_room:
        print(f"Room # {current_room.id} ({current_room.name}): {current_room.description}\n")

        decision = input("Would you like to visit the next room? Would you like to return to the previous room? Or would you like to end the tour?\n- Enter 'N' to go to the next room.\n- Enter 'P' to return to the previous room.\n- Enter any other key to end the tour.\n")

        if decision == 'N':
            current_room = current_room.next_node
        elif decision == 'P':
            current_room = current_room.prev_node
        else:
            input("\nYou've decided to end the tour. Enter any key to continue...\n")
            break

    input("\nYou've reached the end of the tour of Flatiron campus! Enter any key to continue...\n")

def option_2_function():
    print("You selected Option 2!")