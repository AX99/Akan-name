import json
from dateutil.parser import parse
from datetime import datetime as date

#Load the json file with the days and corresponding names
data = json.load(open("akannames.json"))


gender = input("\nAre you Male or Female? (M/F): ")
dob = input("\nEnter your date of birth in this format: 01-Jan-1980: ")


#User input checks 

if gender.upper().strip() not in ("M","F"):
    raise Exception("\n\nYou didn't enter the correct gender. \n\n")
    
try:
    dayName = parse(dob).strftime("%A")
    akanName = data[dayName][gender.upper()]    
except:
    print('\n\nYou didn\'t enter your date of birth correctly\n\n')
    
    

#Print Values - exception if variables not set
try:
    print(
        """
        You were born on a %s
        Your Akan name is %s
        """
        % (dayName, akanName))
except :
    pass

