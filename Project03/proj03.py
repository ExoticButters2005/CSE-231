#######################################################################
#   CSE 231 Project 3
#
#   Start loop for location input
#       Introduction input
#       Location input
#       Taking general input that is true for every location
#       Checking location
#
#       Case 1: Square footage only
#       Formulas used for calculation
#       Print mortgage information
#       Request for amortization and follow-up information if asked
#
#       Case 2: Both are available
#       Formulas used for calculation
#       Print mortgage information
#       Request for amortization and follow-up information if asked

#       Case 3: Maximum monthly payment only
#       Formulas used for calculation
#       Print mortgage information
#
#       Case 4: Not enough information
#       Print message
#
#       Ask if the user needs another attempt
#######################################################################

NUMBER_OF_PAYMENTS = 360
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

# Start loop for location input
KEEP_GOING_TEXT = "Y"
while KEEP_GOING_TEXT == "Y":

    # Introduction input
    print('''\nMORTGAGE PLANNING CALCULATOR\n============================ ''')
    print("\nEnter a value for each of the following items or type 'NA' if unknown ")

    # Location input
    LOCATIONS_TEXT = input("\nWhere is the house you are considering "
                           "(Seattle, San Francisco, Austin, East Lansing)? ")

    # Taking general input that is true for every location
    SQUARE_FOOTAGE_TEXT = input('\nWhat is the maximum square footage '
                                'you are considering? ')
    if SQUARE_FOOTAGE_TEXT.isdigit():
        SQUARE_FOOTAGE_TEXT = float(SQUARE_FOOTAGE_TEXT)
    MAX_MONTHLY_PAYMENT_TEXT = input('\nWhat is the maximum monthly '
                                     'payment you can afford? ')
    if MAX_MONTHLY_PAYMENT_TEXT.isdigit():
        MAX_MONTHLY_PAYMENT_TEXT = float(MAX_MONTHLY_PAYMENT_TEXT)
    DOWN_PAYMENT_TEXT = input('\nHow much money can you put'
                              ' down as a down payment? ')
    if DOWN_PAYMENT_TEXT.isdigit():
        DOWN_PAYMENT_TEXT = float(DOWN_PAYMENT_TEXT)
    else:
        DOWN_PAYMENT_TEXT = float(0)
    APR_TEXT = input('\nWhat is the current annual percentage rate? ')
    if APR_TEXT == "NA":
        APR_TEXT = APR_2023
    else:
        APR_TEXT = float(float(APR_TEXT) / 100)

    # Checking location
    if LOCATIONS_TEXT == "East Lansing":
        PRICE_PER_SQ_FOOT = EAST_LANSING_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = EAST_LANSING_PROPERTY_TAX_RATE
    elif LOCATIONS_TEXT == "Seattle":
        PRICE_PER_SQ_FOOT = SEATTLE_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = SEATTLE_PROPERTY_TAX_RATE
    elif LOCATIONS_TEXT == "Austin":
        PRICE_PER_SQ_FOOT = AUSTIN_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = AUSTIN_PROPERTY_TAX_RATE
    elif LOCATIONS_TEXT == "San Francisco":
        PRICE_PER_SQ_FOOT = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = SAN_FRANCISCO_PROPERTY_TAX_RATE
    else:
        PRICE_PER_SQ_FOOT = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = AVERAGE_NATIONAL_PROPERTY_TAX_RATE
        LOCATIONS_TEXT = "the average U.S. housing market"
        print("\nUnknown location. Using national averages "
              "for price per square foot and tax rate.")

    # Case 1: Square footage only
    if MAX_MONTHLY_PAYMENT_TEXT == "NA"\
            and SQUARE_FOOTAGE_TEXT != "NA":

        # Formulas used for calculation
        HOME_COST = SQUARE_FOOTAGE_TEXT * PRICE_PER_SQ_FOOT
        PRINCIPAL_AMOUNT = HOME_COST - DOWN_PAYMENT_TEXT
        PROPERTY_TAX = HOME_COST * PROPERTY_TAX_RATE
        MONTHLY_TAXES = PROPERTY_TAX / 12
        INTEREST_RATE_PER_MONTH = APR_TEXT / 12
        MONTHLY_PAYMENT = (PRINCIPAL_AMOUNT *
                           (INTEREST_RATE_PER_MONTH * (
                                   1 + INTEREST_RATE_PER_MONTH)
                            ** NUMBER_OF_PAYMENTS) / (
                                   (1 + INTEREST_RATE_PER_MONTH)
                                   ** NUMBER_OF_PAYMENTS - 1))
        TOTAL_PAYMENT_PER_MONTH = MONTHLY_PAYMENT + MONTHLY_TAXES

        # Print mortgage information
        print(f"\n\nIn {LOCATIONS_TEXT}, "
              f"an average {SQUARE_FOOTAGE_TEXT:,.0f} sq. foot"
              f" house would cost ${HOME_COST:,.0f}.")
        print(f"A 30-year fixed rate mortgage with a down payment of"
              f" ${DOWN_PAYMENT_TEXT:,.0f} at {(APR_TEXT * 100):,.1f}"
              f"% APR results")
        print(f"\tin an expected monthly payment of ${MONTHLY_TAXES:,.2f}"
              f" (taxes) + ${MONTHLY_PAYMENT:,.2f} (mortgage payment) "
              f"= ${TOTAL_PAYMENT_PER_MONTH:,.2f}")

        # Request for amortization and follow-up information if asked
        AMORTIZATION_TEXT = input("\nWould you like to print the monthly payment schedule (Y or N)? ")
        if AMORTIZATION_TEXT == "Y":  # If customer ask for the table
            print("\n{:^7}|{:^12}|{:^13}|{:^14}"
                  .format("Month", "Interest", "Payment", "Balance"))
            print("================================================")
            REMAINING_LOAN_AMOUNT = PRINCIPAL_AMOUNT
            MONTH_NUMBER = 0
            while True:
                MONTH_NUMBER += 1
                PAYMENT_TO_INTEREST = REMAINING_LOAN_AMOUNT * APR_TEXT / 12
                PAYMENT_TO_LOAN = MONTHLY_PAYMENT - PAYMENT_TO_INTEREST
                print("{:>7}| ${:^9,.2f} | ${:^10,.2f} | ${:^11,.2f}"
                      .format(MONTH_NUMBER, PAYMENT_TO_INTEREST,
                              PAYMENT_TO_LOAN, REMAINING_LOAN_AMOUNT))
                if REMAINING_LOAN_AMOUNT - PAYMENT_TO_LOAN <= 0:
                    break
                REMAINING_LOAN_AMOUNT = \
                    REMAINING_LOAN_AMOUNT - PAYMENT_TO_LOAN

        # Case 2: Both are available
    elif MAX_MONTHLY_PAYMENT_TEXT != "NA" \
            and SQUARE_FOOTAGE_TEXT != "NA":

        # Formulas used for calculation
        HOME_COST = SQUARE_FOOTAGE_TEXT * PRICE_PER_SQ_FOOT
        PRINCIPAL_AMOUNT = HOME_COST - DOWN_PAYMENT_TEXT
        PROPERTY_TAX = HOME_COST * PROPERTY_TAX_RATE
        MONTHLY_TAXES = PROPERTY_TAX / 12
        INTEREST_RATE_PER_MONTH = APR_TEXT / 12
        MONTHLY_PAYMENT = (PRINCIPAL_AMOUNT *
                           (INTEREST_RATE_PER_MONTH * (
                                   1 + INTEREST_RATE_PER_MONTH)
                            ** NUMBER_OF_PAYMENTS) / (
                                   (1 + INTEREST_RATE_PER_MONTH)
                                   ** NUMBER_OF_PAYMENTS - 1))
        TOTAL_PAYMENT_PER_MONTH = MONTHLY_PAYMENT + MONTHLY_TAXES

        # print mortgage information
        print(f"\n\nIn {LOCATIONS_TEXT}, an average {SQUARE_FOOTAGE_TEXT:,.0f}"
              f" sq. foot house would cost ${HOME_COST:,.0f}.")
        print(f"A 30-year fixed rate mortgage with a down payment of"
              f" ${DOWN_PAYMENT_TEXT:,.0f} at {(APR_TEXT * 100):,.1f}% APR results")
        print(f"\tin an expected monthly payment of ${MONTHLY_TAXES:,.2f} (taxes) "
              f"+ ${MONTHLY_PAYMENT:,.2f} (mortgage payment)"
              f" = ${TOTAL_PAYMENT_PER_MONTH:,.2f}")
        if MAX_MONTHLY_PAYMENT_TEXT > TOTAL_PAYMENT_PER_MONTH:
            print(f"Based on your maximum monthly payment of"
                  f" ${MAX_MONTHLY_PAYMENT_TEXT:,.2f} you can afford this house.")
        else:
            print(f"Based on your maximum monthly payment of"
                  f" ${MAX_MONTHLY_PAYMENT_TEXT:,.2f} you cannot afford this house.")

        # Request for amortization and follow-up information if asked
        AMORTIZATION_TEXT = input("\nWould you like to print the monthly payment schedule (Y or N)? ")
        if AMORTIZATION_TEXT == "Y":  # If customer ask for the table
            print("\n{:^7}|{:^12}|{:^13}|{:^14}"
                  .format("Month", "Interest", "Payment", "Balance"))
            print("================================================")
            REMAINING_LOAN_AMOUNT = PRINCIPAL_AMOUNT
            MONTH_NUMBER = 0
            while True:
                MONTH_NUMBER += 1
                PAYMENT_TO_INTEREST = REMAINING_LOAN_AMOUNT * APR_TEXT / 12
                PAYMENT_TO_LOAN = MONTHLY_PAYMENT - PAYMENT_TO_INTEREST
                print("{:>7}| ${:^9,.2f} | ${:^10,.2f} | ${:^11,.2f}"
                      .format(MONTH_NUMBER, PAYMENT_TO_INTEREST,
                              PAYMENT_TO_LOAN, REMAINING_LOAN_AMOUNT))
                if REMAINING_LOAN_AMOUNT - PAYMENT_TO_LOAN <= 0:
                    break
                REMAINING_LOAN_AMOUNT = \
                    REMAINING_LOAN_AMOUNT - PAYMENT_TO_LOAN
        # Case 3: Maximum monthly payment only
    elif MAX_MONTHLY_PAYMENT_TEXT != "NA" \
            and SQUARE_FOOTAGE_TEXT == "NA":

        # Formulas used for calculation
        INITIAL_SQUARE_FOOTAGE = float(100)
        TOTAL_PAYMENT_PER_MONTH = 0
        while TOTAL_PAYMENT_PER_MONTH <= MAX_MONTHLY_PAYMENT_TEXT:
            INITIAL_SQUARE_FOOTAGE += 1
            HOME_COST = INITIAL_SQUARE_FOOTAGE * PRICE_PER_SQ_FOOT
            PRINCIPAL_AMOUNT = HOME_COST - DOWN_PAYMENT_TEXT
            PROPERTY_TAX = HOME_COST * PROPERTY_TAX_RATE
            MONTHLY_TAXES = PROPERTY_TAX / 12
            INTEREST_RATE_PER_MONTH = APR_TEXT / 12
            MONTHLY_PAYMENT = (PRINCIPAL_AMOUNT *
                               (INTEREST_RATE_PER_MONTH * (
                                       1 + INTEREST_RATE_PER_MONTH)
                                ** NUMBER_OF_PAYMENTS) / (
                                       (1 + INTEREST_RATE_PER_MONTH)
                                       ** NUMBER_OF_PAYMENTS - 1))
            TOTAL_PAYMENT_PER_MONTH = MONTHLY_PAYMENT + MONTHLY_TAXES

        # Prevent overprice
        INITIAL_SQUARE_FOOTAGE -= 1
        HOME_COST = INITIAL_SQUARE_FOOTAGE * PRICE_PER_SQ_FOOT

        # print mortgage information
        print(f"\n\nIn {LOCATIONS_TEXT}, a maximum monthly payment"
              f" of ${MAX_MONTHLY_PAYMENT_TEXT:,.2f} "
              f"allows the purchase of a house of {INITIAL_SQUARE_FOOTAGE:,.0f} sq. feet"
              f" for ${HOME_COST:,.0f}")
        print(f"\t assuming a 30-year fixed rate mortgage with a ${DOWN_PAYMENT_TEXT:,.0f} "
              f"down payment at {(APR_TEXT * 100):.1f}% APR.")

        # Case 4: Not enough information
        # Print message
    else:
        print("\nYou must either supply a desired square footage or a maximum"
              " monthly payment. Please try again.")
        continue
    # Ask if the user needs another attempt
    KEEP_GOING_TEXT = input("\nWould you like to make another attempt (Y or N)? ").upper()
