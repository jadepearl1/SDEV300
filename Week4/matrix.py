'''
Jade Pearl
Lab 4
SDEV 300

This program demonstrates the use of numpy/Pandas. The user inputs matrices and performs
different choices on them such as addition, subtraction, multiplication, and element by element
multiplication. The program takes the users phone number and zipcodes and validates as necessary.
'''
import sys
import pandas as pd
import numpy as np

def main():
    '''
    The main function
    '''
    print('***************** Welcome to the Python Matrix Application *****************')
    while True:
        print('Do you want to play the Matrix Game?')
        yes_no = input('Enter Y for Yes or N for No:\n')
        while yes_no not in ['Y', 'y', 'N', 'n']:
            yes_no = input('Invalid input. Enter Y for Yes or N for No:\n')
        if yes_no.lower() != 'y':
            print('***************** Thanks for playing Python Numpy *****************')
            sys.exit()

        phone = input('Enter your phone number (XXX-XXX-XXXX or (XXX) XXX-XXXX):\n')
        while not valid_phone(phone):
            phone = input('Your phone number is not in the correct format. Please reenter:\n')

        zip_code = input('Enter your zipcode +4 (XXXXX-XXXX):\n')
        while not valid_zip(zip_code):
            zip_code = input('Your zipcode is not the correct format. Please re-enter:\n')

        enter_matrices()

def valid_phone(phone):
    '''
    This function uses input validation to ensure that the user enters a phone number in the proper
    formatting
    '''
    #create a regular expression that allows XXX-XXX-XXXX or (XXX) XXX-XXXX. The space in the
    #second format is REQUIRED to work
    phone_format = r'^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$'
    return any(pd.Series(phone).str.match(phone_format))

def valid_zip(zip_code):
    '''
    This function uses input validation to ensure that the user enters a zipcode in the proper
    formatting
    '''
    zip_format = r'^\d{5}-\d{4}$'
    return any(pd.Series(zip_code).str.match(zip_format))

def enter_matrices():
    '''
    This function prompts the user to enter two matrices and calls the necessary functions
    '''
    #create the matrixes
    print('Enter your first 3x3 matrix:')
    m1 = generate_matrix()
    print('Your first 3x3 matrix is:')
    print_matrix(m1)

    print('Enter your second 3x3 matrix:')
    m2 = generate_matrix()
    print('Your second 3x3 matrix is:')
    print_matrix(m2)

    #print a menu for the user to choose from and have them enter a valid choice
    print("Select a Matrix choice from the list below:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Matrix Multiplication")
    print("d. Element by element multiplication")

    choice = input().lower()
    while choice not in ['a', 'b', 'c', 'd']:
        #ensure that they enter a letter between a and d
        choice = input('Invalid input. Please enter a letter from a to d: ').lower()

    ops(m1, m2, choice)

def generate_matrix():
    '''
    Allows the user to create a 3x3 matrix
    '''
    matrix = []
    for _ in range(3):
        row = input().split()
        # Validate if each value is numeric. Allow for float or integer input
        while not all(val.replace('.', '', 1).isdigit() for val in row):
            print("Invalid input. Please enter numeric values only.")
            row = input().split()
        matrix.append([float(val) for val in row])
    return np.array(matrix)

def print_matrix(matrix):
    '''
    Prints a provided matrix to the screen
    '''
    for row in matrix:
        #does not print a decimal or decimal places unless a float is entered
        print(' '.join(map(lambda x: f'{int(x)}' if x.is_integer() else f'{x:.2f}', row)))

def ops(m1, m2, choice):
    '''
    This function takes the user's menu option and performs the necessary operation on the matrices
    they created
    '''
    if choice.lower() == 'a':
        result = np.add(m1, m2)
        print("You selected Addition. The results are:")
    elif choice.lower() == 'b':
        result = np.subtract(m1, m2)
        print("You selected Subtraction. The results are:")
    elif choice.lower() == 'c':
        result = np.matmul(m1, m2)
        print("You selected Matrix Multiplication. The results are:")
    elif choice.lower() == 'd':
        result = np.multiply(m1, m2)
        print("You selected Element by element multiplication. The results are:")
    else:
        print("Invalid choice selected.")
        return

    print_matrix(result)
    #find the transpose using numpy
    transpose = np.transpose(result)
    print("The Transpose is:")
    print_matrix(transpose)
    #find the means of each row and column
    row_means = np.mean(result, axis=1)
    col_means = np.mean(result, axis=0)

    print("The row and column mean values of the results are:")
    #print with reasonable formatting. MNumbers do not print with decimals unless it is a float
    print(f"Row: {', '.join(map(lambda x: f'{int(x)}' if x.is_integer() else f'{x:.2f}',
row_means))}")
    print(f"Column: {', '.join(map(lambda x: f'{int(x)}' if x.is_integer() else f'{x:.2f}',
col_means))}")

if __name__ == "__main__":
    main()
