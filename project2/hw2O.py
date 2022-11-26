##Name: Jonathan Le, ID: 26713365
##Date: Oct 15, 2021
import math
def main():
	n=eval(input("Please enter N (>2): "))
	k=eval(input("Please enter even K (2<=K<N): "))
	print("Lucas Terms:")
	print("The Nth term of Lucas is:",seriesP(2,1,n))
	print("Fibonacci Terms:")
	print("The Nth term of Fibonacci is:",seriesP(0,1,n))
	g=(1+math.sqrt(5))/2
	print("Golden Ratio:",g)
	print("Fn-k:",series(0,1,n-k))
	print("Fn+k:",series(0,1,n+k))
	print("Left hand side:",series(0,1,n-k)+series(0,1,n+k))
	print("Lk:",series(2,1,k))
	print("Fn",series(0,1,n))
	print("Right hand side:",series(2,1,k)*series(0,1,n))
	f1,f2=1,0
	for i in range(n+1):
		if i==0:
			f=f2
		elif i==1:
			f=f1
		else:
			f=f1+f2
			f2,f1=f1,f
	f2e=f2
	f1e=f1
	err=(f1e/f2e)-g
	print("F_err:",abs(round(err,k)))
def seriesP(f2,f1,a):
	for i in range(a+1):
		if i==0:
			f=f2
		elif i==1:
			f=f1
		else:
			f=f1+f2
			f2,f1=f1,f
		print(f)
	return f
def series(f2,f1,a):
	for i in range(a+1):
		if i==0:
			f=f2
		elif i==1:
			f=f1
		else:
			f=f1+f2
			f2,f1=f1,f
	return f
main()
