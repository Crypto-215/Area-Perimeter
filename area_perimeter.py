# Author: Caleb Bull
# Date: 31-10-2025
# Version 1

# Calculate the area and perimeter using data provided
# Code that tests whether the data given is valid

'''def fence_length(question, min):
    error = f"Whoops, that's not an integer above 0."
    while True:
        try:
            response = int(input(question))
            # if response > 0
            if min < response:
                break # This stops the loop

            else:
                print(f"{error}\n")

        except ValueError:
            print(f"{error}\n")
    return response # This makes the response available to be used

fence_width = fence_length("Enter the width of your fencing in meters: ", 0)

fence_height = fence_length("\nEnter the height of your fencing in meters: ", 0)

perimeter = 2*(fence_height + fence_width)

area = fence_height * fence_width

print(f"\n{perimeter}")

print(area)'''

# Create a greeting (v2)

name = input("Hello! What is your name? ")
print(f"Hey {name}!")
keep_going = "continue"
while keep_going == "continue":
    # Covert answer to lowercase using .lower()
    proceed = input(f"Would you like try out my Area/Perimeter Calculator? ") .lower()
    if proceed == "yes" or proceed == "y":
        print("That's great!")
        keep_going = ""

    elif proceed == "no" or proceed == "n":
        print("That's OK. Maybe another time.")
        keep_going = "done"

    else: # Error Message
        print("I'm not sure I understand...")

def fence_length(question, min):
    error = f"Whoops, that's not a number above 0."
    while True:
        try:
            response = float(input(question))
            # if response is above 0
            if min < response:
                break # This stops the loop

            else:
                print(f"{error}")

        except ValueError:
            print(f"{error}")
    return response # This makes the response available to be used

while keep_going == "": # To make sure program stops when user doesn't want to use calculator
    fence_width = fence_length("\nEnter the width of your fencing in meters: ", 0)
    fence_height = fence_length("Enter the height of your fencing in meters: ", 0)

    perimeter = 2 * (fence_height + fence_width)
    area = fence_height * fence_width

    print(f"\nThe perimeter of your fencing is {perimeter} meters")
    print(f"The area of your fencing is {area} squared meters.")

    keep_going = input("\nPress <ENTER> to do the calculator again, or any other key to quit. ")

print(f"\nThat's it then, have a nice day {name}!")