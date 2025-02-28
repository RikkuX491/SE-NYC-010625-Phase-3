#!/usr/bin/env python3

from helpers import (
    exit_program,
    interact_with_hotels_data,
    interact_with_reviews_data,
    initialize_data
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
            # break
            # return
        elif choice == "1":
            interact_with_hotels_data()
        elif choice == "2":
            interact_with_reviews_data()
        else:
            print("Invalid choice! Please try again!")

    # print("Breaking from the while True loop...")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Interact with Hotels")
    print("2. Interact with Reviews")

if __name__ == "__main__":
    initialize_data()
    main()
    # print("Program ends here...")