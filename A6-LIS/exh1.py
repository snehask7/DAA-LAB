"""Exhaustive Search
1. Design an algorithm to find LengthES(j), the length of LIS(j), the longest increasing
sequence that ends at A[j]. Implement the algorithm LengthES(j)."""
  
from itertools import chain, combinations
def gencomb(arr):
	return chain.from_iterable(combinations(arr, r) for r in range(len(arr)+1))
def LengthES(arr,k):	
	n=len(arr[:k+1])
	maxlen=0
	allcomb=gencomb(arr[:k+1])
	for l in allcomb:
		flag=1
		for j in range(1,len(l)):
			if(l[j]<l[j-1]):
				flag=0
				break
		if flag==1:
			if len(l)>maxlen:
				maxlen=len(l)	
	return maxlen
		
arr=[]
n=int(input("Enter the number of numbers: "))
for i in range(int(n)):
	arr.append(int(input()))
for k in range(n):
	print("LIS("+str(k)+"): "+str(LengthES(arr,k)))

"""
OUTPUT

Enter the number of numbers: 8
5
2
8
6
3
6
9
7
LIS(0): 1
LIS(1): 1
LIS(2): 2
LIS(3): 2
LIS(4): 2
LIS(5): 3
LIS(6): 4
LIS(7): 4
"""
