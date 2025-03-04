# Asking the user to input different types of information related to food
# The input() function displays a prompt and waits for user input.

# Getting the name of a food item from the user
nameFood = input("Enter the name of the food: ")

# Getting the type of plant from which the food is made
nameTypeOfPlant = input("Enter the name of the type of plant: ")

# Getting the method of cooking
methodOfCooking = input("Enter the method of cooking: ")

# Getting the name of a DIY item (likely for creativity or decoration)
nameItem = input("Enter the name of a DIY item: ")

# Printing a message that combines all the user inputs to create a sentence
# The print() function joins multiple values separated by commas, automatically adding spaces between them.
print("Menu", nameFood, "because it's made from", nameTypeOfPlant, "and", methodOfCooking, "it.")
