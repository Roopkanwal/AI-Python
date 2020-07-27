# Ask for User's name
name=input("What is your name?")

# Ask for User's year of birth
birth_year=input("When you were born?")

# Greet User with Hello
print(f"Hello,{name}")

# Calculate and tell age of User
from datetime import datetime
this_year = datetime.now().year
age=this_year-int(birth_year)
print(f"You must be {age}")

# Say Goodbye to user
print("Goodbye!")