"""5. Write a function TraceLIS(n) that returns the LIS of A[0:n] as a list. This function constructs the LIS of A[0:n] by tracing pedecessor array P[] starting from n.
. Implement TraceLIS as a recursive function"""
def TraceLIS(arr,pred,index,maxarr,counter):
	if index==-1:
		return maxarr
	else:
		maxarr[counter]=arr[index]
		counter-=1
		return TraceLIS(arr,pred,pred[index],maxarr,counter)


def LengthDP(arr):
	n=len(arr)
	length=[0 for i in range(n)]
	length[0]=1
	pred=[-1 for i in range(n)]
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
	maxarr=[0 for i in range(0,maxi)]
	counter=maxi-1
	return TraceLIS(arr,pred,index,maxarr,counter)
arr=[]
n=input("Enter the number of numbers: ")
for i in range(int(n)):
	arr.append(int(input()))

print("The maximum length subsequence is: ",LengthDP(arr))

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
