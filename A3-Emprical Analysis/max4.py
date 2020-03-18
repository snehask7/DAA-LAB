"""4. Suppose an algorithm maintains the maximum suffix sum of all subarrays A[0:j] for 0 ≤
j ≤ n in a table suffix max. We can compute them in a single scan of the array.
suffix_max [j] = max (suffix_max [j-1]+A[j-1], 0)
2
Using table suffix max, we can compute the maximum subarray sum of A[0:j] in a single
scan of the array using
subarray_max (A, j) = max (subarray_max (A,j-1), suffix_max [j])
Construct algorithm max_subarray_sum_linear using this idea and implement it. Show that
the algorithm runs in linear time, O(n). Do empirical analysis of the algorithm."""

def max_subarray_sum_linear(a):
	maxsum=-10000
	suffix_max=[0 for i in range(len(a))]
	suffix_max[0]=a[0]
	for i in range(1,len(a)):
		suffix_max [i] = max (suffix_max [i-1]+a[i], 0)	
	return max(suffix_max)
print("input array: [-2,-4,3,-1,5,6,-7,-2,4,3,2],maximum subarray sum: ",max_subarray_sum_linear([-2,-4,3,-1,5,6,-7,-2,4,3,2]))
print("input array: [-2,-4,-3],maximum subarray sum: ",max_subarray_sum_linear([-2,-4,-3]))
print("input array: [-2,-4,3],maximum subarray sum: ",max_subarray_sum_linear([-2,-4,3]))

"""
input array: [-2,-4,3,-1,5,6,-7,-2,4,3,2],maximum subarray sum:  13
input array: [-2,-4,-3],maximum subarray sum:  0
input array: [-2,-4,3],maximum subarray sum:  3
"""