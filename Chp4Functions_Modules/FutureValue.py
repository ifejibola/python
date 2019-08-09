import math
import os
import sys
import requests

print(sys.executable)
# Display welcome message

def calculate_future_value(monthly_investment, yearly_interest, years=20):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    return future_value

def main():
    print("Welcome to the Future Value Calculator")
    print()

    choice = "y"
    while choice.lower() == "y":

        # GET input from the user
        monthlyInvestment = float(input("Enter a monthly investment: \t"))
        yearlyInterestRate = float(input("Enter a yearly interest rate: \t"))
        years = int(input("Enter numner of years: \t\t"))

        # Display the result
        future_value = calculate_future_value(
            monthlyInvestment, yearlyInterestRate, years
        )
        print( "Future value: \t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wnats to continue
        choice = input("Continue (y/n)?: ")
        print()
    print("Bye!")


# if this module is the main module 
# call the main() function
if __name__ == "__main__":
    main()
