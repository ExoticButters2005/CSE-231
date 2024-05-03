 ###########################################################

    #  Computer Project #2
    # import math library
    #  While True loop
    #    prompt for an answer(string) input
    #    prompt for a code(string) input
    #    input an integer
    # billing calculations for each galactic code
    # summary
    

    ###########################################################

import math
INTERGALACTIC_BANNER = """
Welcome to SpaceX Galactic Car Extravaganza!

Prepare for an interstellar joyride with our cosmic cruisers!
At the prompt, please enter:
- Galactic code (XV, ET, SI)
- Days of your interstellar joyride
- Odometer at liftoff
- Odometer at touchdown
"""
# string prompts
print(INTERGALACTIC_BANNER)
INTERGALACTIC_PROMPT = "Ready for an out-of-this-world adventure (Y/X)? "
INVALID_CODE_PROMPT = "\n*** Invalid galactic code. Retry! ***"    
CUSTOMER_CODE_INPUT = "\nGalactic code (XV, ET, SI): "
RENTAL_DAYS_INPUT = "\nNumber of days (int): "
START_ODOMETER_INPUT = "\nOdometer at liftoff (int): "
END_ODOMETER_INPUT = "\nOdometer at touchdown (int):   "
INTERGALACTIC_BANNER = """
Welcome to SpaceX Galactic Car Extravaganza!

Prepare for an interstellar joyride with our cosmic cruisers!
At the prompt, please enter:
- Galactic code (XV, ET, SI)
- Days of your interstellar joyride
- Odometer at liftoff
- Odometer at touchdown
"""

print(INTERGALACTIC_BANNER)
INTERGALACTIC_PROMPT = "Ready for an out-of-this-world adventure (Y/X)? "
INVALID_CODE_PROMPT = "\n*** Invalid galactic code. Retry! ***"    
CUSTOMER_CODE_INPUT = "\nGalactic code (XV, ET, SI): "
RENTAL_DAYS_INPUT = "\nNumber of days (int): "
START_ODOMETER_INPUT = "\nOdometer at liftoff (int): "
END_ODOMETER_INPUT = "\nOdometer at touchdown (int):   "
answer = input(INTERGALACTIC_PROMPT)
# main loop
while True:
    # answer check
    
    if answer != 'Y': 
        print(INVALID_CODE_PROMPT)
        answer = input(INTERGALACTIC_PROMPT)

    if answer == 'X':
        break

    # galactic code input
    while True:
        galactic_code = input(CUSTOMER_CODE_INPUT).upper()
        # galactic code check
        if galactic_code == 'XV' or galactic_code == 'ET' or galactic_code == 'SI':
            break
        print(INVALID_CODE_PROMPT)
        
    
    days = int(input(RENTAL_DAYS_INPUT))
    odometer_start = int(input(START_ODOMETER_INPUT))
    odometer_end = int(input(END_ODOMETER_INPUT))

    # billing calculations
    # Calculate light-years driven
    light_years = round(float(odometer_end - odometer_start)/10, 1)
    # changes light year to float and round to nearest 1 decimal place

    if galactic_code == 'XV':
        
        base_charge = float(40 * days)
        light_year_charge = 0.25 * light_years 
    elif galactic_code == 'ET':
       
        base_charge = float(60 * days)
        average_ly_per_day = light_years / days
        light_year_charge = 0 if average_ly_per_day <= 100 else 0.25 * (light_years - 100 * days)
    else: # SI
        
        
        weeks = math.ceil(days / 7) #calculate by weeks or fractions of weeks
        base_charge = float(190 * weeks)
        average_ly_per_week = light_years / weeks
        if average_ly_per_week <= 900:
            light_year_charge = 0
        elif average_ly_per_week <= 1500:
            light_year_charge = 100 * weeks # exceeds 900
        else:
            light_year_charge = 200 * weeks + 0.25 * (light_years - 1500 * weeks) #exceeds 1500

    total_charge = base_charge + light_year_charge 

    # print results
    print("\nGalactic traveler summary:")
    print("\tCode:", galactic_code)
    print("\tDays in orbit:", days)
    print("\tLiftoff odometer:", odometer_start)
    print("\tTouchdown odometer:", odometer_end)
    print("\tLight-years traveled:", light_years)
    print("\tCost in star credits: $", round(total_charge, 2)) # rounded to 2 decimal places
print("\nThank you for entrusting us with your joyride!")
    

    




