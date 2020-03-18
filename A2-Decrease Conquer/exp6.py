#6. Modify fast power (x, n) to mat power (x, n) for computing the power of a matrix x raised to n.
def mat_mul(a,b): #function to multiply matrices
	res=[[0 for x in range(o)] for y in range(o)]
	for x in range(o):
		for y in range(o):
			for z in range(o):
				res[x][y]=res[x][y]+(a[x][z]*b[z][y])
	return res
	
def mat_power(x,n): #function to find the matrix after power applied
	if n==0:
		return unit
	elif n%2==0:
		return mat_mul(mat_power(x,n/2),mat_power(x,n/2))
	else:
		return mat_mul(mat_power(x,n-1),x)
		
def unitmat():#to create the unit matrix
	for i in range(o):
		unit[i][i]=1

o=int(input("Enter the order of the matrix: "))
#DATA INPUT
x=[[0 for i in range(o)] for j in range(o)]
unit=[[0 for i in range(o)] for j in range(o)]
print("\nINPUT DATA FOR MATRIX")
for i in range(o):
	print("\nROW",int(i+1))
	for j in range(o):
		x[i][j]=int(input("Enter number: "))

print("\nCONTENTS OF MATRIX: ")
for i in range(o):
	for j in range(o):
		print(x[i][j],end=" ")
	print("\n")
unitmat()
n=int(input("Enter the power to which you want to raise the matrix: "))
x=mat_power(x,n)

#DISPLAYING THE RESULT
print("\nRESULT: ")
for i in range(o):
	for j in range(o):
		print(x[i][j],end=" ")
	print("\n")

"""
OUTPUT

Enter the order of the matrix: 3

INPUT DATA FOR MATRIX

ROW 1
Enter number: 2
Enter number: 3
Enter number: 4

ROW 2
Enter number: 5
Enter number: 4
Enter number: 2

ROW 3
Enter number: 1
Enter number: 2
Enter number: 3

CONTENTS OF MATRIX: 
2 3 4 

5 4 2 

1 2 3 

Enter the power to which you want to raise the matrix: 3

RESULT: 
202 225 222 

273 304 300 

132 147 145 
"""