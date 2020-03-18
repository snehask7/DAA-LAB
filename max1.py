"""1.Design a exhaustive enumeration/brute-force algorithm and implement it. Name it max subarray sum cubic. The algorithm keeps track of the maximum subarray sum in an accumulator. It enumerates all possible subarrays, computes the sum for each subarray, and
updates the maximum subarray sum. Design an algorithm sum(A, i, j) for computing the sum of the items of a subarray A[i:j]
and use it in max subarray sum cubic. You may implement sum(A, i, j) as a function and call it. Or you may use the algorithm directly inside max subarray sum cubic. Show that the algorithm runs in cubic time, O(n 3 )."""

def max_subarray_sum_cubic(a):
	maxsum=0
	lindex=0
	hindex=0
	n=len(a)
	for i in range(0,n-1):
		for j in range(i+1,n):
			subsum=sum(a,i,j)
			if subsum>maxsum:
				maxsum=subsum
				lindex=i
				hindex=j
	if a[n-1]>maxsum:
		maxsum=a[n-1]
		lindex=n-1
		hindex=n
	print("The input array is: ",a)
	print("The maximum subarray sum is: ",maxsum)
	print("The maximum sub array is: a[",lindex,":",hindex,"]")
	print(a[lindex:hindex],"\n\n")
	
def sum(a,i,j):
	sum=0
	for x in range(i,j):
		sum=sum+a[x]
	return sum
			
max_subarray_sum_cubic([-2,-4,3,-1,5,6,-7,-2,4,3,2])
max_subarray_sum_cubic([-2,-4,-3])
max_subarray_sum_cubic([-2,-4,3])
"""OUTPUT

The input array is:  [-2, -4, 3, -1, 5, 6, -7, -2, 4, 3, 2]
The maximum subarray sum is:  13
The maximum sub array is: a[ 2 : 6 ]
[3, -1, 5, 6] 


The input array is:  [-2, -4, -3]
The maximum subarray sum is:  0
The maximum sub array is: a[ 0 : 0 ]
[] 


The input array is:  [-2, -4, 3]
The maximum subarray sum is:  3
The maximum sub array is: a[ 2 : 3 ]
[3] 



"""
