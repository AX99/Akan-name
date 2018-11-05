import json
from datetime import datetime as date

data = json.load(open("ghananames.json"))

#print(data["Monday"]["F"]) FOR Adjoa
gender = input("Are you Male or Female? (M/F): ")
y = int(input("Enter your year of birth: "))
m = int(input("Enter your month of birth (1-12): "))
d = int(input("Enter your day of birth: "))

day_name = date(y, m, d).strftime("%A")
ghana_name = data[day_name][gender.upper()]
print()
print("You were born on a " + day_name)
print("Your Ghanaian name is " + ghana_name)
print()
