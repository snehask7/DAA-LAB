#1. Implement an algorithm using dynamic programming to find the length of LCS.
def lcs(a,b):
	m=len(a)
	n=len(b)
	l=[[0 for i in range(n+1)] for j in range(m+1)]
	for x in range(1,m+1):
		for y in range(1,n+1):
			if a[x-1]==b[y-1]:
				l[x][y]=l[x-1][y-1]+1
			else:
				l[x][y]=max(l[x-1][y],l[x][y-1])
	#print(l)
	return l[m][n]
print("Enter the elements in array A: ")
a=[int(i) for i in input().split()]
print("Enter the elements in array B: ")
b=[int(i) for i in input().split()]
print("longest common subsequence length: ",lcs(a,b))

"""
OUTPUT

Enter the elements in array A: 
5 3 2 9 7 87 54 12 3
Enter the elements in array B: 
234 76 3 12 3 23 5 87
longest common subsequence length:  3

"""s
