#1. Construct a recursive algorithm power (x, n), to compute x^n , x raised to a non-negative exponent n ≥ 0.

def power(x,n):
	if n==0:#base condition
		return 1
	else:
		return x*power(x,n-1)#recursive function call

print("Calculating x to the power n")
x=int(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))
print("The result is: ")
print(power(x,n))

"""
OUTPUT

Calculating x to the power n
Enter the value of x: 7
Enter the value of n: 5
The result is: 
16807
"""
