# 1. Find any one safe configuration. Use backtracking to do exhaustive search for an answer in the state space of the problem
def safe(r,col,c):
	for j in range(r):
		if 	c[j]==col or abs(r-j)==abs(col-c[j]):	#if no other queen is in that column and no queen is diagonal
			return 0
	return 1

def nqueen(c,r):
	global completed	
	if completed==0:	#used to make sure only 1 safe configutation is found
		q=0
		if r==n:	#if all 8 rows have been filled
			for i in range(n):
				q+=safe(i,c[i],c)	#counts the number of rows that are safe
			if q==n:	#checks if all rows are safe, therefore it is a solution
				print(c)
				completed=1
			return
		for x in range(n):
			c[r]=x
			nqueen(c,r+1)

n=8
c=[-1 for i in range(n)]
completed=0
print("1 safe configuration is: \n")
nqueen(c,0)

"""
OUTPUT

1 safe configuration is: 

[0, 4, 7, 5, 2, 6, 1, 3]
"""
