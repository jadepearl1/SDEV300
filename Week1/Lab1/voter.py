''' Jade Pearl
SDEV 300 Lab 1
This program is a simple voter registration application that asks the user to enter required
information and lets them know that their voter card will be mailed if they are eligible. The 
program must use input validation to determine if the user is eligible to vote and therefore get a
voter registration card '''

import sys

def main():
    '''
    Main function which asks the user their demographic information such as name,
    age, citizenship status, state of residence, and zipcode.
    
    Main calls other functions to check for eligibility and other validations.'''

    print("***********************************************************************************\n")
    print("Welcome to the Pyhton Voter Registration Application.")
    stay_leave()

    first = input("What is your first name?\n")
    #make sure the first name is a string
    while not first.isalpha():
        first = input("Invalid input. What is your first name?\n")
    stay_leave()

    last = input("What is your last name?\n")
    #make sure the last name is a string
    while not last.isalpha():
        last = input("Invalid input. What is your last name?\n")
    stay_leave()

    user_age = input("What is your age?\n")
    #age must be an integer / number
    while not user_age.isdigit() or int(user_age) > 120:
        user_age = input("Invalid input. What is your age?\n")
    age = int(user_age)
    if age < 18:
        not_eligible()
    stay_leave()

    citizen = input("Are you a U.S. Citizen?\n")
    #make sure that the user enters a string
    while citizen not in ("Yes.", "yes.", "No.", "no.", "Yes", "yes", "No", "no"):
        citizen = input("Invalid input. Are you a U.S. Citizen?\n")
        if citizen not in ("Yes.", "yes.", "Yes", "yes"):
            not_eligible()
    stay_leave()

    state = input("In what state do you live? Please input the state intials (Ex. AZ)\n").upper()
    #make sure the state is a string
    while isinstance(state, str) is False or len(state) != 2:
        state = input("Invalid input. In what state do you live?\n").upper()
    if state not in ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL"
    "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT"
    "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
    "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]:
        not_eligible()
    stay_leave()

    user_zip = input("What is your zipcode? (if entering a 9-digit zip, do NOT use the -)\n")
    #make sure the zip code is an int
    while not user_zip.isdigit() or len(user_zip) not in [5, 9]:
        user_zip = input("What is your zipcode?\n")

    name = first + " " + last

    thankyou(name, age, citizen, state, user_zip)

def stay_leave():
    '''
    The stay_leave function holds the prompt asking the user if they wish to continue
    using the application or not and exits the program if not.
    '''
    stay = input("Do you want to continue with the voter application?\n")
    #input validation: if the user says anything but yes, exit the program
    if stay not in ('Yes.', 'Yes', 'yes.', 'yes'):
        stay = input("Are you sure you want to quit?\n")
        if stay in ('Yes.', 'Yes', 'yes.', 'yes'):
            print("Now exiting the application. Thank you!")
            sys.exit()

def not_eligible():
    '''
    The not_eligible function tells the user they are not eligible to vote with an appropriate
    message before exiting the program.
    '''
    print("You are not eligible to vote. Thank you for using the Python Voter Registration \
Application.")
    sys.exit()

def thankyou(name, age, citizen, state, user_zip):
    '''
    Thankyou function thanks the user for using the application and then repeats the information
    entered into the program. It then tells the user that their voter registration card will be
    mailed within 3 weeks before exiting.
    '''
    print("\nThanks for registering to vote. Here is the information we received:")
    print("Name (first last): " + name)
    print("Age: " + str(age))
    print("U.S. Citizen: " + citizen)
    print("State: " + state)
    print("zipcode: " + str(user_zip))
    print("Thanks for trying the Voter Registration Application.")
    print("Your voter registration card should be shipped within 3 weeks.")
    print("**************************************************************************************")
    sys.exit()

if __name__ == "__main__":
    main()
