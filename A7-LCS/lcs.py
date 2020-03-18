#2. Implement an algorithm to backtrace the LCS itself.
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
	maxele=l[m][n]
	seq=[]
	while maxele>0:
		ele=0
		for i in range(1,m+1):
			for j in range(1,n+1):
				if l[i][j]==maxele:
					ele=a[i-1]
					print(ele)	
					break
			if ele!=0:
				break
			
		seq.append(ele)
		maxele=maxele-1
	print(seq[::-1])
	return l[m][n]
				
print("Enter the elements in array A: ")
a=[int(i) for i in input().split()]
print("Enter the elements in array B: ")
b=[int(i) for i in input().split()]
print("longest common subsequence length: ",lcs(a,b))

"""
OUTPUT

Enter the elements in array A: 
3 4 5 6 9
Enter the elements in array B: 
9 4 5
5
4

"""
