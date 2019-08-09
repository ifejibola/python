#!/usr/bin/env python3

import validation as val


def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float("Enter monthly investment: ", 0, 101)
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        years = int(input("Enter number of years:\t\t"))

        # get and display future value
        future_value = val.calculate_future_value(
            monthly_investment, yearly_interest_rate, years
        )

        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")


def get_float(prompt, low, high):
    isValid = True
    while isValid:
        monthlyInvestment = float(input(prompt))

        if monthlyInvestment > low and monthlyInvestment <= high:
            isValid = False
            return monthlyInvestment
        else:
            print("Monthly investment is too high or low")


if __name__ == "__main__":
    main()
