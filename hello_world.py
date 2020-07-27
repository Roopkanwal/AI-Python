name=input("What is your name?")
birth_year=input("When you were born?")
print(f"Hello,{name}")

from datetime import datetime
this_year = datetime.now().year
age=this_year-int(birth_year)
print(f"You must be {age}")
print("Goodbye!")