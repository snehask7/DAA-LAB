#2. Construct a Iterative algorithm power (x, n), to compute x^n , x raised to a non-negative exponent n ≥ 0.

def power(x,n):
	res=1
	for i in range(n):
		res=res*x
	return res
print("Calculating x to the power n")
x=int(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))
print("The result is: ")
print(power(x,n))

"""
OUTPUT

Calculating x to the power n
Enter the value of x: 7
Enter the value of n: 6
The result is: 
117649

"""
