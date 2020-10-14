# Oct 12 2020
# Paint Job Estimator
# A painting company has determined that for every 115 square feet
# of wall space, one gallon of paint and eight hours of labor will
# be required.  The company charges $20.00 per hour for labor.
# Write a program that asks the user to enter the square feet of
# wall space to be painted and the price of the paint per gallon.
# The program should display the following data:
#   The number of gallons of paint required
#   The hours of labor required
#   The cost of the paint
#   The labor charges
#   The total cost of the paint job

def main():
    # wall space to be painted.
    square_footage = float(input('Enter the number of square feet to be painted: '))
    # price of the paint per gallon.
    price_gallon = float(input('Enter the price of the paint per gallon: '))

    estimation(square_footage, price_gallon)


def estimation(square_footage, price_gallon):
    # 115 sq ft = 1 gallon + 8 hrs of labor ,labor is $20 per hour
    num_gallons = square_footage / 115.0
    hours_labor = num_gallons * 8
    total_price_gallon = num_gallons * price_gallon
    total_labor = hours_labor * 20
    final_total = total_price_gallon + total_labor
    print("Gallons of Paint: " + str(round(num_gallons, 2)))
    print("Hours of labor: " + str(round(hours_labor, 2)))
    print("Cost of paint: $" + str(round(total_price_gallon, 2)))
    print("Labor charges: $" + str(round(total_labor, 2)))
    print("Your total estimated price for your paint job is $" + str(round(final_total, 2)))

main()
input('Please press Enter to exit')