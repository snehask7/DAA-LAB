"""7. Fibonacci numbers can be expressed using matrix notation:Using this idea, implement a function fib (n) to compute Fn, the nth Fibonacci number.
Use mat power for matrix expoentiation."""
def mat_mul(a,b):
	res=[[0 for x in range(2)] for y in range(2)]
	for x in range(2):
		for y in range(2):
			for z in range(2):
				res[x][y]=res[x][y]+(a[x][z]*b[z][y])
	return res
def mat_power(x,n):
	if n==0:
		return unit
	elif n%2==0:
		return mat_mul(mat_power(x,n/2),mat_power(x,n/2))
	else:
		return mat_mul(mat_power(x,n-1),x)
def fib(n):
	mat=[[0,1],[1,1]]
	mat=mat_power(mat,n)
	return mat[0][1]
unit=[[1,0],[0,1]]
x=int(input("Enter the term: "))
print(fib(x))

"""
OUTPUT

Enter the term: 8
21

Enter the term: 11
89

"""