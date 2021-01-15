import json
from dateutil.parser import parse
from datetime import datetime as date


def run_script(gender, dob):
    #Load the json file with the days and corresponding names
    data = json.load(open("app/static/scripts/akannames.json"))

    # gender = input("\nAre you Male or Female? (M/F): ")

    # if gender.upper().strip() not in ("M","F"):
    #     raise Exception("\n\nYou didn't enter the correct gender. \n\n")

    # dob = input("\nEnter your date of birth in this format: 01-Jan-1980: ")
        
    try:
        dayName = parse(dob).strftime("%A")
        akanName = data[dayName][gender.upper()]   
        return dayName, akanName 
    except:
        print('\n\nYou didn\'t enter your date of birth correctly\n\n')
        

    #Print Values - exception if variables not set
    # try:
    #     print(
    #         """
    #         You were born on a %s
    #         Your Akan name is %s
    #         """
    #         % (dayName, akanName))
    # except :
    #     pass

    

