# Ask for user's name
name=input("What is your name?")

# Ask for user's year of birth
birth_year=input("When you were born?")

# Greet user with Hello
print(f"Hello,{name}")

# Calculate and tell age of user
from datetime import datetime
this_year = datetime.now().year
age=this_year-int(birth_year)
print(f"You must be {age}")

# Say Goodbye to user
print("Goodbye!")