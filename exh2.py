"""2. Using LengthES(j), find the lenth of the LIS of the array A[0:n]. Test it."""
  
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
		
arr=[2, 4, 3, 5, 1, 7, 6, 9, 8]
print("Array is: ",arr," Length of LIS: "+str(LengthES(arr,len(arr))))

arr=[5, 1, 5, 7, 2, 4, 9, 8]
print("Array is: ",arr," Length of LIS: "+str(LengthES(arr,len(arr))))

arr=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]
print("Array is: ",arr," Length of LIS: "+str(LengthES(arr,len(arr))))
"""
OUTPUT

Array is:  [2, 4, 3, 5, 1, 7, 6, 9, 8]  Length of LIS: 5
Array is:  [5, 1, 5, 7, 2, 4, 9, 8]  Length of LIS: 4
Array is:  [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]  Length of LIS: 9

"""
