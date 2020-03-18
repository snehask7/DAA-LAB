"""Dynamic Programming
1. Using Dynamic Programming, design an algorithm LengthDP(j) to find the length of the
LIS(j), longest increasing sequence that ends at A[j] for j = 0,1,2,. . .,n-1. Implement the algorithm LengthDP(j)."""
def LengthDP(arr,k):
	n=len(arr)
	length=[0 for i in range(n)]
	length[0]=1
	for i in range(n):
		maxi=0
		for  j in range(i):
			if arr[j]<arr[i] and length[j]>maxi:
				maxi=length[j]
		length[i]=maxi+1

	return length[k]
arr=[]
n=input("Enter the number of numbers: ")
for i in range(n):
	arr.append(int(input()))
for k in range(n):
	print("LIS("+str(k)+"): "+str(LengthDP(arr,k)))

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
