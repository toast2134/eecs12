# Programmer: Jonathan Le
# Date: Oct 15, 2021
#
# import math library
import math

# main function
# calculates Lucas sequence and Fibonacci sequence for n values
# calculates Golden Ratio
# 
def main():
	# get user input -> eval() is dangerous
	n=eval(input("Please enter N (>2): "))
	k=eval(input("Please enter even K (2<=K<N): "))
	
	# Lucas - 2, 1, 3, 4, 7...
	l1,l2=1,2
	print("Lucas Terms:")
	
	# prints Lucas terms from 0th to nth
	for i in range(n+1):
		if i==0:
			l=l2
		elif i==1:
			l=l1
		else:
			l=l1+l2
			l2,l1=l1,l
		print(l)

	print("The Nth term of Lucas is:",l)
	
	# Fibonacci - 0, 1, 1, 2, 3, 5, 8...
	f1,f2=1,0	
	print("Fibonacci Terms:")

	# prints Fibonacci terms from 0th to nth
	for i in range(n+1):
		if i==0:
			f=f2
		elif i==1:
			f=f1
		else:
			f=f1+f2
			f2,f1=f1,f
		print(f)
	
	# setting golden ratio error calculation
	f1e=f1
	f2e=f2
	print("The Nth term of Fibonacci is:",f)
	
	# Actual Golden Ratio
	g=(1+math.sqrt(5))/2
	print("Golden Ratio:",g)
	
	# Left side of Fibonacci
	# prints F(n-k) term
	f1,f2=1,0	
	for i in range(n-k+1):
		if i==0:
			f=f2
		elif i==1:
			f=f1
		else:
			f=f1+f2
			f2,f1=f1,f
	fL=f
	print("Fn-k:",fL)
	
	# prints F(n+k) term
	f1,f2=1,0
	for i in range(n+k+1):
		if i==0:
			f=f2
		elif i==1:
			f=f1
		else:
			f=f1+f2
			f2,f1=f1,f
	fU=f
	print("Fn+k:",fU)

	# adds the two previous calculations to get the "left hand side" of fibonacci series
	print("Left hand side:",fU+fL)
	
	# Right side error
	# prints L(k) (kth term in lucas series)
	l1,l2=1,2
	for i in range(k+1):
		if i==0:
			l=l2
		elif i==1:
			l=l1
		else:
			l=l1+l2
			l2,l1=l1,l
	print("Lk:",l)
		
	# prints F(n) (nth term of fibonacci sequence)
	f1,f2=1,0	
	for i in range(n+1):
		if i==0:
			f=f2
		elif i==1:
			f=f1
		else:
			f=f1+f2
			f2,f1=f1,f
	print("Fn",f)

	# "Right hand side" calculated by multiplying L(k) and F(n)
	print("Right hand side:",f*l)
	
	# Golden Ratio error calculation
	# rounds to kth terms
	err=(f1e/f2e)-g
	print("F_err:",abs(round(err,k)))
	
main()
