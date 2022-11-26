# Programmer: Jonathan Le
# Date: Sept 28, 2021
# 
# Overall Logic is the same, just uses float() to evaluate input instead of eval
# main function
def main():
	# user prompt
	print("This program calculates the value of a 10-year investment every year")

	# get user input -> store as floats since we know they are float values
	# doesn't use eval()
	principal = float(input("Enter the principal amount: "))
	ir = float(input("Enter the half-yearly compounded interest rate (less than 1): "))
	investr = float(input("Enter the half-yearly investment rate (less than 1): "))

	# calculate constants
	invests = principal * investr
	ir = 1 + (0.5 * ir) 

	# prints balance each year 0 -> 9
	for i in range(10): 
		principal = (principal * ir + invests) * ir + invests
		print("The balance after year", i+1, "is", principal)

	# prints balance after 10 years
	print("The value after 10 years is:", principal)
main()
