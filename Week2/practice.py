'''Jade Pearl
Week 2 Lab 2
This program is a command line menu-driven python application that allows users to perform math and
security related functions.'''

import sys
import random
import string
from datetime import datetime
import math

def main():
    """
    The main function calls a function to print a menu and prompts the user to pick from it.
    If choice f is entered, the program terminates.
    """
    print("Welcome! Please enter a choice from the menu below! Enter f to exit the program.\n")

    while True:
        print_menu()
        choice = get_valid_choice()

        if choice == "f":
            print("Now exiting the program!")
            sys.exit()
        else:
            process_choice(choice)

def print_menu():
    """
    This function prints the menu to the console.
    """
    print("a. Generate Secure Password")
    print("b. Calculate and Format a Percentage")
    print("c. How many days from today until July 4 2025?")
    print("d. Use the Law of Cosines to calculate the leg of a triangle.")
    print("e. Calculate the volume of a Right Circular Cylinder")
    print("f. Exit program\n")

def get_valid_choice():
    """
    Data validation for the user's menu choice
    """
    choice = input("Enter a menu option or enter f to exit: ")
    while choice.lower() not in ["a", "b", "c", "d", "e", "f"]:
        choice = input("Invalid input. Please enter a choice from the menu below: ")
    return choice.lower()

def process_choice(choice):
    """
    This function takes the user's selected choice and calls the appropriate functions
    """
    if choice == "a":
        length, complexities = get_password_options()
        password_generate(length, complexities)
    elif choice == "b":
        numerator, denominator, places = get_percentage_input()
        percent_calc(numerator, denominator, places)
    elif choice == "c":
        today = datetime.now().date()
        countdown(today)
    elif choice == "d":
        side_a, side_b, angle_c = get_law_dimensions()
        law_of_cosines(side_a, side_b, angle_c)
    elif choice == "e":
        radius, height = get_cylinder_dimensions()
        cylinder(radius, height)

def get_password_options():
    """
    The user is able to enter the length and complexity of the password they wish to have generated
    """
    length = input("Enter the length for your password: ")
    while not length.isdigit() or int(length) < 4:
        length = input("Invalid input. Enter a length of at least 4: ")

    complexity = input("Enter the desired complexity (uppercase, lowercase, numbers, special)"
    + "\n(Type out each word in lowercase with commas separating each word. NO SPACES)\n")
    while not is_valid_complexity(complexity):
        complexity = input("Invalid input. Enter the desired complexity: ")

    return int(length), complexity.lower().split(",")

def is_valid_complexity(complexity):
    """
    Validates the input complexity options.
    """
    valid_options = ["uppercase", "lowercase", "numbers", "special"]
    return all(option in valid_options for option in complexity.split(","))

def get_percentage_input():
    """
    User enters a numerator, denominator, and # decimal places to be used to calculate a percentage
    """
    numerator = input("Enter a numerator: ")
    while not numerator.isdigit():
        numerator = input("Invalid input. Enter a numerator: ")

    denominator = input("Enter a denominator: ")
    while not denominator.isdigit():
        denominator = input("Invalid input. Enter a denominator: ")

    places = input("Enter the number of decimal places: ")
    while not places.isdigit():
        places = input("Invalid input. Enter the number of decimal places: ")

    return int(numerator), int(denominator), int(places)

def get_law_dimensions():
    """
    This function has the user enter two sides and an angle of a triangle to perform law of cosines
    """
    side_a = input("Enter the length of side a: ")
    while side_a.isalpha():
        side_a = input("Invalid input. Enter the length of side a: ")

    side_b = input("Enter the length of side b: ")
    while side_b.isalpha():
        side_b = input("Invalid input. Enter the length of side b: ")

    angle_c = input("Enter the degree of angle c: ")
    while angle_c.isalpha():
        angle_c = input("Invalid input. Enter the degree of angle c: ")

    return float(side_a), float(side_b), float(angle_c)

def get_cylinder_dimensions():
    """
    User must enter the dimensions of a cylinder
    """
    radius = input("Enter the radius of the cylinder: ")
    while radius.isalpha():
        radius = input("Invalid input. Enter the radius of the cylinder: ")

    height = input("Enter the height of the cylinder: ")
    while height.isalpha():
        height = input("Invalid input. Enter the height of the cylinder: ")

    return float(radius), float(height)

def password_generate(length, complexities):
    """
    Generates a secure password based on user input.
    """
    characters = ""

    for complexity in complexities:
        if complexity == "uppercase":
            characters += string.ascii_uppercase
        elif complexity == "lowercase":
            characters += string.ascii_lowercase
        elif complexity == "numbers":
            characters += string.digits
        elif complexity == "special":
            characters += string.punctuation

    if not characters:
        print("Invalid complexities. Please choose at least one option.")
        return

    secure_password = ''.join(random.choice(characters) for _ in range(length))
    print("Here is your password: " + secure_password + "\n")

def percent_calc(num, denom, places):
    """
    Calculates a percentage from given numerator, denominator, and decimal places.
    """
    percent = (int(num) / int(denom)) * 100
    new_percent = round(percent, int(places))
    print("Here is your percentage: " + str(new_percent) + "%\n")

def countdown(today):
    """
    Countdown calculates and prints the number of days until 07/04/2025.
    """
    target = datetime(2025, 7, 4).date()
    days_left = (target - today).days
    print("There are " + str(days_left) + " days until July 4th, 2025.\n")

def law_of_cosines(side_a, side_b, angle_c):
    """
    This function calculates the law of cosines.
    """
    angle_c = math.radians(angle_c)

    c_squared = side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_c)
    side_c = math.sqrt(c_squared)
    side_c = round(side_c, 2)
    print("The length of side c is " + str(side_c) + "\n")

def cylinder(radius, height):
    """
    This function calculates the volume of the cylinder.
    """
    volume = (math.pi * float(radius)**2) * float(height)
    volume = round(volume, 2)
    print("The volume of the cylinder is " + str(volume) + "\n")

if __name__ == "__main__":
    main()
