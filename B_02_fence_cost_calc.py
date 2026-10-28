# Ask user for width and loop until they 
# enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True: 

        try:
            # Ask the user for a number
            response = float(input(question))

            # Check if the width is more than zero
            if response > 0:
                return response
            else:
                print(error) 

        except ValueError:
            print(error)

# Main routine goes here...

keep_going = ""
while keep_going == "":

    # Get width and height and cost
    width = num_check("\nPlease enter your width: ")
    length = num_check("\nPlease enter your height: ")
    cost = num_check("\nPlease enter the price per metre of fencing: ")

    # Calculate area / perimeter / cost
    area = width * length
    perimeter = 2 * (width + length)
    total_cost = perimeter * cost

    # Display output
    print()
    print(f"\nThe area is {area} units.")
    print(f"\nThe perimeter is {perimeter} units.")
    print(f"\nThe total cost of your fencing is {total_cost} dollars.")

    # Ask user if they want to keep going
    print()
    keep_going = input("\nPress enter to keep going or any key to quit. ")
    print()

print("Thank you for using the fence cost calculator")
    