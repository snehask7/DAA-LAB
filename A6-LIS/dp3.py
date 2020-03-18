"""4. Algorithm LengthDP() maintains L[j], the length of the LIS that ends at A[j]. In addition,
now we also want to maintain the predecessor P[j] of A[j] in the LIS that ends at A[j].
Modify LengthDP(j) to maintain both L[j] and P[j]."""
def LengthDP(arr,k):
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
	# print(length)
	# print(pred)
	return length[k],pred[k]
arr=[]
n=input("Enter the number of numbers: ")
for i in range(n):
	arr.append(int(input()))
for k in range(n):
	l,p=LengthDP(arr,k)
	print("L["+str(k)+"]: "+str(l) +"   P["+str(k)+"]: "+str(p) )

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
L[0]: 1   P[0]: 0
L[1]: 1   P[1]: 0
L[2]: 2   P[2]: 0
L[3]: 2   P[3]: 0
L[4]: 2   P[4]: 1
L[5]: 3   P[5]: 4
L[6]: 4   P[6]: 5
L[7]: 4   P[7]: 5

"""
