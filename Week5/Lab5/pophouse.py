'''
Jade Pearl
SDEV 300
Lab 5
'''
import sys
import pandas as pd
import matplotlib.pyplot as plt

def main():
    '''
    This main function prints out the main menu to the python data analysis and calls a function to
    validate the user's choice. Once a valid choice is found, it calls functions accordingly
    '''
    print('***************** Welcome to the Python Data Analysis App *****************')
    while True:
        print('Select the file you want to analyze:')
        print('1. Population Data')
        print('2. Housing Data')
        print('3. Exit the Program')

        choice = get_valid_choice()
        if int(choice) == 3:
            print('***************** Thanks for using the Data Analysis App *****************')
            sys.exit()
        elif int(choice) == 1:
            population_menu()
        elif int(choice) == 2:
            housing_menu()

def get_valid_choice():
    '''
    Recycled from one of my previous programs and edited to fit the criteria
    Makes sure that the choice entered by the user from the menu is a number
    '''
    #Using a flag, make sure the user selects a valid choice from the menu
    valid_choice = False
    while valid_choice is False:
        choice = input("Enter a number between 1-3: ")
        if choice.isdigit():
            if int(choice) in [1, 2, 3]:
                #if a valid chouce is made, mark as True to exit the while loop
                valid_choice = True
            else:
                continue
    #return the user's choice to the main function for analysis
    return choice

def population_menu():
    '''
    Opens PopChange.csv and asks what part of it the user wants analyzed
    '''
    print('You have entered Population Data.')
    #using a variable to hold the data, read the file using pandas read_csv function
    data = pd.read_csv('PopChange.csv')
    while True:
        #print the menu and take input until the user exits
        print('Select the Column you want to analyze: ')
        print('a. Pop Apr 1')
        print('b. Pop Jul 1')
        print('c. Change Pop')
        print('d. Exit Column\n')
        #input validation
        valid_choice = False
        while valid_choice is False:
            pop_choice = input('Enter a letter between a and d: ')
            if pop_choice.isalpha():
                if pop_choice.lower() in ['a', 'b', 'c', 'd']:
                    #if a valid chouce is made, mark as True to exit the while loop
                    valid_choice = True
                else:
                    continue

        if pop_choice.lower() == 'd':
            print('You selected to exit the column menu')
            break
        if pop_choice.lower() == 'a':
            print('You selected Pop Apr 1')
            read_col_data(data['Pop Apr 1'])
        elif pop_choice.lower() == 'b':
            print('You selected Pop Jul 1')
            read_col_data(data['Pop Jul 1'])
        elif pop_choice.lower() == 'c':
            print('You selected Change Pop')
            read_col_data(data['Change Pop'])

def housing_menu():
    '''
    Opens Housing.csv and asks what part of it the user wants analyzed
    '''
    print('You have entered Housing Data.')
    #using a variable to hold the data, read the file using pandas read_csv function
    data = pd.read_csv('Housing.csv')
    while True:
        #print the menu and take input until the user exits
        print('Select the Column you want to analyze:')
        print('a. AGE')
        print('b. BEDRMS')
        print('c. BUILT')
        print('d. ROOMS')
        print('e. UTILITY')
        print('f. Exit Column\n')
        #input validation
        valid_choice = False
        while valid_choice is False:
            house_choice = input('Enter a letter between a and f: ')
            if house_choice.isalpha():
                if house_choice.lower() in ['a', 'b', 'c', 'd', 'e', 'f']:
                    #if a valid chouce is made, mark as True to exit the while loop
                    valid_choice = True
                else:
                    continue

        if house_choice.lower() == 'f':
            print('You selected to exit the column menu')
            break
        if house_choice.lower() == 'a':
            print('You selected AGE')
            read_col_data(data['AGE'])
        elif house_choice.lower() == 'b':
            print('You selected BEDRMS')
            read_col_data(data['BEDRMS'])
        elif house_choice.lower() == 'c':
            print('You selected BUILT')
            read_col_data(data['BUILT'])
        elif house_choice.lower() == 'd':
            print('You selected ROOMS')
            read_col_data(data['ROOMS'])
        elif house_choice.lower() == 'e':
            print('You selected UTILITY')
            read_col_data(data['UTILITY'])

def read_col_data(column):
    '''
    Reads the column data and calculates the statistics of the coulumn before printing them out to
    the console
    '''
    stats = {
        'Count': column.count(),
        'Mean': round(column.mean(), 1),
        'Standard Deviation': round(column.std(), 1),
        'Min': round(column.min(), 1),
        'Max': round(column.max(), 1)
    }

    #print the statistics
    print('The statistics for this column are:')
    for stat, value in stats.items():
        print(f"{stat} = {value}")

    #histogram printing
    print('The Histogram of this column is now displayed')
    plt.hist(column, bins = 50, color='#008fd5', edgecolor='black')
    plt.show()

if __name__ == '__main__':
    main()
