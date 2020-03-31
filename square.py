
def addnumber(ms,r,c):	#function to add a number to the magic square
	if r==n or c==n:
		return 1
	else:
		for i in range(1,n+1):
			ms[r][c]=i
			if issafe(ms,r,c)==1:		
				if c==n-1:
					if addnumber(ms,r+1,0)==1:	#row has been filled completely
						return 1
				else:
					if addnumber(ms,r,c+1)==1:	#row has not been filled completely
						return 1
			else:
				ms[r][c]=0
		return 0

def issafe(ms,r,c):	#function to check if a number doesnt voilate the safe condition
	#check within the row 
	for i in range(n):
		if ms[r][c]==ms[r][i] and i!=c:
			return 0	#not safe
	#check within the column
	for i in range(n):
		if ms[r][c]==ms[i][c] and i!=r:
			return 0	#not safe
	return 1

def display(ms):
	for i in range(n):
		print(ms[i])
	print("\n")
n=9
ms=[[0 for i in range(n)] for j in range(n)]

addnumber(ms,0,0)
display(ms)

"""
OUTPUT

[1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 1, 4, 3, 6, 5, 8, 9, 7]
[3, 4, 1, 2, 7, 8, 9, 5, 6]
[4, 3, 2, 1, 8, 9, 6, 7, 5]
[5, 6, 7, 8, 9, 1, 2, 3, 4]
[6, 5, 8, 9, 1, 7, 3, 4, 2]
[7, 8, 9, 5, 2, 3, 4, 6, 1]
[8, 9, 6, 7, 4, 2, 5, 1, 3]
[9, 7, 5, 6, 3, 4, 1, 2, 8]

"""