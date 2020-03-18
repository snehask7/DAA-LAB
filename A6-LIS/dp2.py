"""3. Introduce A[n] = infinity and modify LengthDP() to return the length of the LIS of A[0:n]."""
def LengthDP(arr):
	n=len(arr)
	length=[0 for i in range(n)]
	length[0]=1
	for i in range(n):
		maxi=0
		for  j in range(i):
			if arr[j]<arr[i] and length[j]>=maxi:
				maxi=length[j]
		length[i]=maxi+1

	return length[n-2]
arr=[]
n=input("Enter the number of numbers: ")
for i in range(n):
	arr.append(int(input()))
arr.append(100000000)
print("LIS: "+str(LengthDP(arr)))

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
