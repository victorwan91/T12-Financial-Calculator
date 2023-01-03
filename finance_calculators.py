# Import built-in module math.
import math

# Print messages of the detail of the two financial options - investment and bond.
# Declare a new variable "choice" to ask for a user input to choose investment or bond to proceed.
print("Investment - to calculate the amount of interest you will earn on your investment.")
print("Bond - to calculate the amount you will have to pay on a home loan.")
choice = input ("Choose ether 'investment' or 'bond' from the menu to proceed: ")

# If the input is "investment" converted to lower case, then print message.
if choice.lower() == "investment":
    print("You have chosen 'investment', please answer the following questions.")

    # Then declare 3 new variables, "deposit", "interest_rate" and "years".
    # Ask for user's answers for each question regarding deposit, interest rate and years.
    deposit = float(input("How much are you depositing (R): "))
    interest_rate = float(input("Interest rate (%): "))
    years = int(input("The number of years you plan on investing: "))

    # And ask the user to choose the interest type - "simple" or "compound" and store in variable "interest_choice".
    interest_choice = input("Please select 'Simple' or 'compound' interest. Type (simple/compound): ")

    # If the user's input is "simple" converted to lower case.
    # Calculate the total and store in "total_investment" with equation A = P (1 + r * t) and print message.
    # Where A = total, P = deposit, r = interest rate in percentage (r/100) and t = years
    if interest_choice.lower() == "simple":
        total_investment = deposit * (1 + (interest_rate/100) * years)
        print(round(total_investment, 2))

    # Else, it means user chose "compound".
    # Calculate total for compound and store in "total_investment" and print message.
    # Equation used is A = P (1 + r) ^ t
    else:
        total_investment = deposit * math.pow((1 + interest_rate/100), years)
        print(round(total_investment, 2))

# Else if "choice" input is "bond" converted to lower case, then print message.
elif choice.lower() == "bond":
    print("You have chosen 'Bond', please answer the following question.")

    # Declare 3 new variables - "house_value", "interest_rate", "month_repay".
    # Ask for user's answer input to each question.
    house_value = float(input("The present value of the house (R): "))
    interest_rate = float(input("The interest rate: "))
    month_repay = int(input("The number of months you plan to take to repay the bond: "))

    # Calculate total and store in a new variable "total_bond" and print message using f-string
    # Equation used: x = (i*P)/(1 - (1+i)^(-n))
    # where x = total, i = monthly interest rate (divide i by 12 months and 100 for percentage), n = number of months
    total_bond = ((interest_rate/1200) * house_value) / (1 - (1 + (interest_rate/1200)) ** (-month_repay))
    print(f"You will have to repay R{round(total_bond, 2)} each month.")

# If the user input in "choice" is neither "investment" nor "bond", then use else statement and print an error message
else:
    print("Your input is invalid, please try again.")