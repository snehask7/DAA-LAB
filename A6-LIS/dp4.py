"""5. Write a function TraceLIS(n) that returns the LIS of A[0:n] as a list. This function constructs the LIS of A[0:n] by tracing pedecessor array P[] starting from n.
. Implement TraceLIS as a iterative function"""
def TraceLIS(arr,pred,index):
	maxarr=[]
	while index!=0:
		maxarr.append(arr[index])
		index=pred[index]
	return maxarr


def LengthDP(arr):
	n=len(arr)
	length=[0 for i in range(n)]
	length[0]=1
	pred=[0 for i in range(n)]
	for i in range(n):
		maxi=0
		for  j in range(i):
			if arr[j]<arr[i] and length[j]>maxi:
				maxi=length[j]
				pred[i]=j

		length[i]=maxi+1
	index=0
	maxi=0
	for i in range(n):
		if length[i]>maxi:
			maxi=length[i]
			index=i
	return TraceLIS(arr,pred,index)
arr=[]
n=input("Enter the number of numbers: ")
for i in range(int(n)):
	arr.append(int(input()))
lismax=LengthDP(arr)
print("The maximum length subsequence is: ",lismax[::-1])

"""
Enter the number of numbers: 8
5                               
2
8
6
3
6
9
7
The maximum length subsequence is:  [2, 3, 6, 9]



"""
