"""3. Design a divide and conquer algorithm for maximum subarray sum: Divide the array
A[low:high] into halves A[low:mid] and A[mid:high]. Find the maximum subarrays of
the two halves recursively. The maximum subarray of A[low:high] is one of the three:
1. Maximum subarray of A[low:mid],
2. Maximum subarray of A[mid:high],
3. Maximum subarray overlapping both halves.
To calculate the maximum subarray overlapping the two halves, compute the maximum suffix A[i:mid] of the first half and the maximum prefix A[mid:j of the second half. A[i:j]
is the maximum subarray overlapping the two halves.
Design algorithm max subarray sum linearithmic using divide-and-conquer and implement it. Show that the algorithm runs in linearithmic time, O(n log n). Do empirical analysis
of the algorithm."""

import random
import timeit

def maxval(a,b,c):
	if a>b:
		if a>c and a>0:
			return a
		elif c>0:
			return c
	elif b>0:
		return b
	return 0
def max_subarray_sum_linearithmic(a,low,high):
	if low==high:
		return a[low]
	mid=int((low+high)/2)
	return maxval(max_subarray_sum_linearithmic(a,low,mid),
	max_subarray_sum_linearithmic(a,mid+1,high),
	max_overlap(a,low,high,mid))

def max_overlap(a,low,high,mid):
	leftsum=-100
	rightsum=0
	sum=0
	for i in range(mid,low-1,-1):
		sum=sum+a[i]
		if sum>leftsum:
			leftsum=sum
	sum=0
	for i in range(mid+1,high+1):
		sum=sum+a[i]
		if sum>rightsum:
			rightsum=sum
	return leftsum+rightsum

"""Easier code:def maxsubarrsum(a,l,u):
	if(u==l):
		return a[l]

	mid=(l+u)//2
	lss=rss=-1000
	sum=0
	for i in range (mid,l-1,-1):
		sum+=a[i]
		lss=max(lss,sum)
	
	sum=0
	for i in range (mid+1,u+1):
		sum+=a[i]
		rss=max(rss,sum)
	return max(maxsubarrsum(a,l,mid),maxsubarrsum(a,mid+1,u),lss+rss)




n=int(input("Enter n : "))
a=[]
for i in range(n):
	a.append(int(input("Enter the element:")))
print("Max subarray sum is:",maxsubarrsum(a,0,n-1))




"""

print("input array: [-2,-4,3,-1,5,6,-7,-2,4,3,2],maximum subarray sum: ",max_subarray_sum_linearithmic([-2,-4,3,-1,5,6,-7,-2,4,3,2],0,10))
print("input array: [-2,-4,-3],maximum subarray sum: ",max_subarray_sum_linearithmic([-2,-4,-3],0,2))
print("input array: [-2,-4,3],maximum subarray sum: ",max_subarray_sum_linearithmic([-2,-4,3],0,2))

"""
output

input array: [-2,-4,3,-1,5,6,-7,-2,4,3,2],maximum subarray sum:  13
input array: [-2,-4,-3],maximum subarray sum:  0
input array: [-2,-4,3],maximum subarray sum:  3
"""
