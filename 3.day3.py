# Asking the user to input their name
# The input() function displays a message and waits for the user to type something.
yourName = input("Name: ")

# Asking the user to input the current year
# Again, input() captures what the user types and stores it in a variable.
whatYear = input("What's year is it?: ")

# Printing a message that combines the user's name and the year they entered
# The print() function takes multiple arguments separated by commas.
# This method does not strictly concatenate, but it joins elements with spaces automatically.
print(yourName, "think it's", whatYear)