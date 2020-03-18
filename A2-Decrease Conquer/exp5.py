"""Construct a function mat_mul (a, b) that multiples two matrices a and b and returns the
product matrix. Represent a matrix by a list of lists. The function should check for valid
input, and raise execption if the input is invalid."""

def mat_mul(a,b):
	res=[[0 for x in range(l)] for y in range(i)]
	for x in range(i):
		for y in range(l):
			for z in range(j):
				res[x][y]=res[x][y]+(a[x][z]*b[z][y])
	return res
	

print("MATRIX MULTIPLICATION")
cont=1

#INPUT OF MATRIX DIMENSIONS
while(cont==1):
	i=int(input("Enter the number of rows in matrix 1: "))
	j=int(input("Enter the number of columns in matrix 1: "))
	k=int(input("Enter the number of rows in matrix 2: "))
	l=int(input("Enter the number of columns in matrix 2: "))
	if(j!=k):
		print("Number of columns in matrix 1 and number of rows in matrix 2 not the same!!! Enter again!!")
	else:	
		cont=0

#initialization of matrix
a=[[0 for x in range(j)] for y in range(i)]
b=[[0 for x in range(l)] for y in range(k)]
product=[[]]

#INPUT OF MATRIX VALUES
print("\nINPUT DATA FOR MATRIX 1")

for x in range(i):
	print("\nROW",int(x+1))
	for y in range(j):
		a[x][y]=int(input("Enter number: "))
print("\nINPUT DATA FOR MATRIX 2")
for x in range(k):
	print("\nROW",int(x+1))
	for y in range(l):
		b[x][y]=int(input("Enter number: "))
		
#DISPLAYING DATA
print("\nCONTENTS OF MATRIX 1: ")
for x in range(i):
	for y in range(j):
		print(a[x][y],end=" ")
	print("\n")	
print("\nCONTENTS OF MATRIX 2: ")
for x in range(k):
	for y in range(l):
		print(b[x][y],end=" ")
	print("\n")
product=mat_mul(a,b)
print("\nRESULT OF MULTIPLICATION: ")
for x in range(i):
	for y in range(l):
		print(product[x][y],end=" ")
	print("\n")

	
"""

OUTPUT

MATRIX MULTIPLICATION
Enter the number of rows in matrix 1: 3
Enter the number of columns in matrix 1: 4
Enter the number of rows in matrix 2: 3
Enter the number of columns in matrix 2: 4
Number of columns in matrix 1 and number of rows in matrix 2 not the same!!! Enter again!!
Enter the number of rows in matrix 1: 4
Enter the number of columns in matrix 1: 3
Enter the number of rows in matrix 2: 3
Enter the number of columns in matrix 2: 2

INPUT DATA FOR MATRIX 1

ROW 1
Enter number: 2
Enter number: 3
Enter number: 4

ROW 2
Enter number: 1
Enter number: 2
Enter number: 5

ROW 3
Enter number: 4
Enter number: 3
Enter number: 2

ROW 4
Enter number: 1
Enter number: 2
Enter number: 4

INPUT DATA FOR MATRIX 2

ROW 1
Enter number: 3
Enter number: 2

ROW 2
Enter number: 4
Enter number: 1

ROW 3
Enter number: 1
Enter number: 2

CONTENTS OF MATRIX 1: 
2 3 4 

1 2 5 

4 3 2 

1 2 4 


CONTENTS OF MATRIX 2: 
3 2 

4 1 

1 2 


RESULT OF MULTIPLICATION: 
22 15 

16 14 

26 15 

15 12 
"""