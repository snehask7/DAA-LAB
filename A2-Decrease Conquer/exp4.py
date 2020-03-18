#4. Construct a faster iterative algortithm fast power (x, n) to compute the power of x raised to n
def fast_power(x,n):
	res1=1
	res2=1
	if n%2==0:#if even
		for i in range(int(n/2)):
			res1=res1*x
		for i in range(int(n/2)):
			res2=res2*x
		return res1*res2
	else:#if odd
		for i in range(n-1):
				res1=res1*x
		return res1*x

print("Calculating x to the power n")
x=int(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))
print("The result is: ")
print(fast_power(x,n))

"""
OUTPUT

Calculating x to the power n
Enter the value of x: 7
Enter the value of n: 6
The result is: 
117649

"""
