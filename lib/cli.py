#!/usr/bin/env python3

from helpers import (
    exit_program,
    traverse_through_pages,
    traverse_through_rooms
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            traverse_through_pages()
        elif choice == "2":
            traverse_through_rooms()
        else:
            print("Invalid choice! Please try again!")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Interact with Page data")
    print("2. Interact with Room data")

if __name__ == "__main__":
    main()