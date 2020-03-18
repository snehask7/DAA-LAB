#3. Construct a faster recursive algortithm fast power (x, n) to compute the power of x raised to n
def fast_power(x,n):
	if n==0:
		return 1
	elif n%2==0:#if even
		return fast_power(x,n/2) * fast_power(x,n/2)
	else:#if odd
		return fast_power(x,n-1)*x
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
