# Programmer: Jonathan Le
# Date: 9/28/2021
#
# main function - calculates interest
def main():
    # print program description
	print("This program calculates the future value\nof a 10-year investment.")
    
    # get user input for rates and initial investment
    # used eval() -> but eval is unsafe, should not use normally
	principal = eval(input("Enter the initial investment: "))
	ir = eval(input("Enter the half-yearly compounded interest rate (less than 1): "))
	investr = eval(input("Enter the half-yearly investment rate (less than 1): "))
    
    # calculations to make code below shorter
	invests = principal * investr
	ir  = 1 + (0.5 * ir)
	
    # prints balance each year -> goes from 0 to 9
	for i in range(10):
		principal = (principal * ir + invests) * ir + invests
		print("The balance after year", i+1, "is", principal)
	
    # prints the balance after 10 years
	print("The value after 10 years is:", principal)
	
main()
