# The 'print' function displays text on the screen.
# This line prints a greeting message.
print("Getting to know you!")

# The 'input' function collects user input from the keyboard.
# It pauses execution until the user enters a response and presses Enter.
# The response is stored in variables for later use.
yourName = input("What is your name?: ")  # Stores the user's name.
favouriteFood = input("What is your favourite food?: ")  # Stores the user's favorite food.
favouriteMusic = input("What is your favourite music?: ")  # Stores the user's favorite music.
liveIn = input("Where do you live?: ")  # Stores the user's place of residence.

# Printing an empty line for better readability.
print()

# Printing multiple pieces of information using variables.
print("So you are", yourName)  # Displays the user's name.
print("You are probably hungry for", favouriteFood)  # Displays the user's favorite food.
print("and you are definitely getting your groove on to", favouriteMusic)  # Displays the user's favorite music.
print("So, my friend", yourName)  # Addresses the user as a friend.
print("living in the amazing", liveIn)  # Displays the user's place of residence with emphasis.

# Another empty line for spacing.
print()

# Final message to conclude the interaction.
print("Nice to meet you!")

# Summary:
# This program interacts with the user by asking for their name, favorite food, music preference, and place of residence.
# The responses are stored in variables and later printed in sentences to create a personalized message.
# Using 'input' allows dynamic interaction, and 'print' outputs information to the screen.
# Proper variable naming makes the code clear and readable.