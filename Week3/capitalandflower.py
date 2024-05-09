'''
Jade Pearl
SDEV 300 Lab 3
This program allows a user to serch and display U.S. state capitals, population, and flowers. The
program gives the option to display all states, populations, and flowers; seatch for a specific
state, population, and display the image of its flower; provide a bar graph of the top 5 populted
states showing their population; and update overall state population for a specific state
'''
import sys
from PIL import Image
import matplotlib.pyplot as plt

states_list = [
    ['Alabama', 'Montgomery', 5143033, 'Camellia', 'flowers/AL-camellia.jpg'],
    ['Alaska', 'Juneau', 733536, 'Forget-Me-Not', 'flowers/AK-forget-me-not.jpg'],
    ['Arizona', 'Phoenix', 7497004, 'Saguaro Cactus Blossom', 'flowers/AZ-cactusblossom.jpg'],
    ['Arkansas', 'Little Rock', 3089060, 'Apple Blossom', 'flowers/AR-appleblossom.jpg'],
    ['California', 'Sacramento', 38889770, 'California Poppy', 'flowers/CA-californiapoppy.jpg'],
    ['Colorado', 'Denver', 5914181, 'Rocky Mountain Columbine', 'flowers/CO-rockymtncol.jpg'],
    ['Connecticut', 'Hartford', 3625646, 'Mountain Laurel', 'flowers/CT-mtnlaurel.jpg'],
    ['Delaware', 'Dover', 1044321, 'Peach Blossom', 'flowers/DE-peachblossom.jpg'],
    ['Florida', 'Tallahassee', 22975931, 'Orange Blossom', 'flowers/FL-orangeblossom.jpg'],
    ['Georgia', 'Atlanta', 11145304, 'Cherokee Rose', 'flowers/GA-cherokeerose.jpg'],
    ['Hawaii', 'Honolulu', 1430877, 'Pua Aloalo (Hibiscus)', 'flowers/HI-puaaloalo.jpg'],
    ['Idaho', 'Boise', 1990456, 'Syringa', 'flowers/ID-syringa.jpg'],
    ['Illinois', 'Springfield', 12516863, 'Violet', 'flowers/IL-violet.jpg'],
    ['Indiana', 'Indianapolis', 6892124, 'Peony', 'flowers/IN-peony.jpg'],
    ['Iowa', 'Des Moines', 3214315, 'Wild Rose', 'flowers/IA-wildrose.jpg'],
    ['Kansas', 'Topeka', 2944376, 'Sunflower', 'flowers/KS-sunflower.jpg'],
    ['Kentucky', 'Frankfort', 4540745, 'Goldenrod', 'flowers/KY-goldenrod.jpg'],
    ['Louisiana', 'Baton Rouge', 4559475, 'Magnolia', 'flowers/LA-magnolia.jpeg'],
    ['Maine', 'Augusta', 1402106, 'White Pine', 'flowers/ME-whitepine.jpg'],
    ['Maryland', 'Annapolis', 6196525, 'Black-eyed Susan', 'flowers/MD-blackeyedsusan.jpg'],
    ['Massachusetts', 'Boston', 7020058, 'Mayflower', 'flowers/MA-mayflower.jpg'],
    ['Michigan', 'Lansing', 10041241, 'Apple Blossom', 'flowers/MI-appleblossom.jpg'],
    ['Minnesota', 'St. Paul', 5761530, 'Pink and White Ladys Slipper', 'flowers/MN-ladyslip.jpg'],
    ['Mississippi', 'Jackson', 2940452, 'Magnolia', 'flowers/MS-magnolia.jpg'],
    ['Missouri', 'Jefferson City', 6215144, 'Hawthorn', 'flowers/MO-hawthorn.jpg'],
    ['Montana', 'Helena', 1142746, 'Bitterroot', 'flowers/MT-bitterroot.jpg'],
    ['Nebraska', 'Lincoln', 1988698, 'Goldenrod', 'flowers/NE-goldenrod.jpg'],
    ['Nevada', 'Carson City', 3210931, 'Sagebrush', 'flowers/NV-sagebrush.jpg'],
    ['New Hampshire', 'Concord', 1405105, 'Purple Lilac', 'flowers/NH-purplelilac.jpg'],
    ['New Jersey', 'Trenton', 9320865, 'Purple Violet', 'flowers/NJ-purpleviolet.jpg'],
    ['New Mexico', 'Santa Fe', 2115266, 'Yucca', 'flowers/NM-yucca.jpg'],
    ['New York', 'Albany', 19469232, 'Rose', 'flowers/NY-rose.jpg'],
    ['North Carolina', 'Raleigh', 10975017, 'Dogwood', 'flowers/NC-dogwood.jpg'],
    ['North Dakota', 'Bismarck', 788940, 'Wild Prairie Rose', 'flowers/ND-wildprarierose.jpg'],
    ['Ohio', 'Columbus', 11812173, 'Scarlet Carnation', 'flowers/OH-redcarnation.jpg'],
    ['Oklahoma', 'Oklahoma City', 4088377, 'Oklahoma Rose', 'flowers/OK-oklahomarose.jpg'],
    ['Oregon', 'Salem', 4227337, 'Oregon Grape', 'flowers/OR-oregongrape.jpg'],
    ['Pennsylvania', 'Harrisburg', 12951275, 'Mountain Laurel', 'flowers/PA-mtnlaurel.jpg'],
    ['Rhode Island', 'Providence', 1098082, 'Violet', 'flowers/RI-violet.jpg'],
    ['South Carolina', 'Columbia', 5464155, 'Yellow Jessamine', 'flowers/SC-yellowjessamine.jpg'],
    ['South Dakota', 'Pierre', 928767, 'Pasque Flower', 'flowers/SD-pasque.jpg'],
    ['Tennessee', 'Nashville', 7204002, 'Iris', 'flowers/TN-iris.jpg'],
    ['Texas', 'Austin', 30976754, 'Bluebonnet', 'flowers/TX-bluebonnet.jpg'],
    ['Utah', 'Salt Lake City', 3454232, 'Sego Lily', 'flowers/UT-segolily.jpg'],
    ['Vermont', 'Montpelier', 647818, 'Red Clover', 'flowers/VT-redclover.jpg'],
    ['Virginia', 'Richmond', 8752297, 'American Dogwood', 'flowers/VA-dogwood.jpg'],
    ['Washington', 'Olympia', 7841283, 'Western Rhododendron', 'flowers/WA-rhodo.jpg'],
    ['West Virginia', 'Charleston', 1766107, 'Rhododendron', 'flowers/WV-rhodo.jpg'],
    ['Wisconsin', 'Madison', 5931367, 'Wood Violet', 'flowers/WI-woodviolet.jpg'],
    ['Wyoming', 'Cheyenne', 586485, 'Indian Paintbrush', 'flowers/WY-indianpaintbrush.jpg']
]

def main():
    '''
    The main function prints the menu and prompts the user to make a selection. It then calls
    functions based on the user's choice
    '''
    print("Welcome to the State Capital, Population, and Flower List Application!")
    while True:
        print("\n1. Display All U.S. States in Alphabetical order along with the Capital, State"
          + " Population, and Flower\n")
        print("2. Search for a specific state and display the appropriate Capital name, State"
          + " Population, and an image of the associated State Flower.\n")
        print("3. Provide a Bar graph of the top 5 populated States showing their overall"
          +" population\n")
        print("4. Update the overall state population for a specific state.\n")
        print("5. Exit the program")

        choice = get_valid_choice()

        if int(choice) == 5:
            print("Thank you! Now exiting the program!")
            sys.exit()
        elif int(choice) == 1:
            display_all()
        elif int(choice) == 2:
            search_state()
        elif int(choice) == 3:
            make_graph()
        elif int(choice) == 4:
            update_pop()

def get_valid_choice():
    '''
    Makes sure that the choice entered by the user from the menu is a number or number plus a "."
    '''
    #Using a flag, make sure the user selects a valid choice from the menu
    valid_choice = False
    while valid_choice is False:
        choice = input("Enter a number between 1-5: ")
        if choice.isdigit():
            if int(choice) in [1, 2, 3, 4, 5]:
                #if a valid chouce is made, mark as True to exit the while loop
                valid_choice = True
            else:
                choice = input('Enter a number between 1 and 5: ')
    #return the user's choice to the main function for analysis
    return choice

def display_all():
    '''
    This function carries out the first choice from the menu, displaying all states in alpbabetical
    order with their capitals, populations, and state flowers
    '''
    print("\nHere is the sorted list of U.S. States, Capitals, Populations, and Flowers:")
    sorted_states = sorted(states_list, key=lambda x: x[0]) #This sorts the states by name
    #make a loop to print out each state in the list
    for state in sorted_states:
        print(f"{state[0]}: Capital - {state[1]}, Population - {state[2]}, Flower - {state[3]}")

def search_state():
    '''
    This function will prompt the user to search for a state and then display that state's
    information as well as an image of the state flower
    '''
    state_name = input('\nEnter a state name or abbreviation to search: ')
    while True:
        found = False
        for state in states_list:
            # Check if the input matches either full state name or state abbreviation
            if state[0].lower() == state_name.lower() or state[0].lower() == valid_state\
            (state_name).lower():
                print(f"\nState: {state[0]}, Capital: {state[1]}, Population: {state[2]}, Flower: \
{state[3]}")
                #if the image is found, display the picture
                display_flower(state[4])
                found = True
                break  # Exit the loop after finding the state

        if found:
            break  # Exit the main loop if the state is found
        state_name = input('\nState not Found. Enter a state name or abbreviation to search: ')

def valid_state(state):
    '''
    This function is for when the user enters state initials in option 2. It validates whether or
    not their input is valid.
    '''
    #make a list of valid states for when the user enters abbreviations instead of a full name
    valid_states = {"AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA":
                    "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "FL": 
                    "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", 
                    "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
                    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": 
                    "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", 
                    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
                    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico",
                    "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", 
                    "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", 
                    "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas",
                    "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": 
                    "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"}
    input_state_upper = state.upper()
    return valid_states.get(input_state_upper, state)

def display_flower(img_path):
    '''
    Displays the image of a specified state flower.
    '''
    #using exception handling, make sure the image is found
    try:
        with Image.open(img_path) as img:
            img.show()
    except FileNotFoundError:
        print(f"Image not found at path: {img_path}")

def make_graph():
    '''
    This function represents choice number 3 where the program generates a graph of the top 5
    states in terms of population
    '''
    #in states_list, the program needs to look at the 3rd element which is the population
    #sort the list in descending order of population
    top_search = sorted(states_list, key=lambda x: x[2], reverse=True)
    top_5 = top_search[:5] #this pulls the top 5 states sorted by population
    #pull out the names and population of each state
    names = [state[0] for state in top_5]
    population = [state[2] for state in top_5]

    #create and display the graph
    plt.figure(figsize=(10, 6))
    plt.bar(names, population)
    plt.xlabel('State')
    plt.ylabel('Population (by Millions)')
    plt.title('Top 5 States by Population')
    plt.show()

def update_pop():
    '''
    This function allows the user to specify a state and update its population
    '''
    while True:
        state_name = input('\nEnter a state name or abbreviation to update its population: ')
        state = find_state(state_name)
        #if the state is found, make a loop for finding a valid population
        if state:
            #keep in mind the current population to let the user see how it is changing
            print(f"The current population of {state[0]}: {state[2]}")
            while True:
                try:
                    new_pop = int(input(f"Enter the updated population of {state[0]}: "))
                    if new_pop <= 0:
                        raise ValueError("Population must be a positive number greater than 0")
                    state[2] = new_pop
                    print(f'Population of {state[0]} successfully updated to {state[2]}')
                    break  # Exit the population update loop
                except ValueError:
                    print('Invalid input. Please enter a valid positive integer.')
            #this if statement is in a while loop so a break will be put here to exit the loop if a 
            #state is found and a proper population update is input
            break
        else:
            print('\nState not Found. Please enter a valid state name or abbreviation.')

def find_state(state_name):
    '''
    Finds a state in the states_list based on provided name or abbreviation. Returns None if the
    state isn't found
    '''
    for state in states_list:
        #check if the input matches either full state name or state abbreviation
         if state[0].lower() == state_name.lower() or state[0].lower() == valid_state\
(state_name).lower():
            return state
    return None

if __name__ == "__main__":
    main()
