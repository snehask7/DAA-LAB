"""Algorithm in Question 1 calculates the sum of each subarray in linear time (O(n)). By calculating the sums of all prefixes A[0:i] for 0 ≤ i ≤ n of the array once and saving them in a
table prefix sum, we can calculate sum(A, i, j in constant time, using
sum(A, i, j) = prefix_sum[j] - prefix_sum[i]
Design an algorithm max subarray sum quadratic using this idea and implement it. Show
that the algorithm runs in quadratic time, O(n
2
). Do empirical analysis of the algorithm."""

def  max_subarray_sum_quadratic(a):
	maxsum=0
	lindex=0
	hindex=0
	n=len(a)
	prefix_sum(a)
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
	
def prefix_sum(a):
	psum[0]=a[0]
	for i in range(1,len(a)):
		psum[i]=psum[i-1]+a[i]
def sum(a,i,j):
	return psum[j-1]-psum[i-1]
psum=[0for i in range(100)]		
max_subarray_sum_quadratic([-2,-4,3,-1,5,6,-7,-2,4,3,2])
max_subarray_sum_quadratic([-2,-4,-3])
max_subarray_sum_quadratic([-2,-4,3])
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