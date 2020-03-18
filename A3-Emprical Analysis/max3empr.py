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

def empr():
	n=[10,50,100,1000,5000]
	for i in range(5): #5 different input sizes
		sum=0
		a=[]
		for m in range(5): #m is taken as 5
			for j in range(n[i]):#to generate the list of size n
				a.append(random.randint(-100,100))
			start = timeit.default_timer()
			maxsum=max_subarray_sum_linearithmic(a,0,n[i]-1)
			stop = timeit.default_timer()
			sum=sum+(stop-start)
		avg=sum/5
		ratio=avg/pow(n[i],3)
		print("\nn: ",n[i],"\nAVG Runtime: ",avg,"RATIO: ",ratio)

print("EMPRICAL ANALYSIS: ")	
empr()			

"""
output

EMPRICAL ANALYSIS: 

n:  10 
AVG Runtime:  1.55439998707152e-05 RATIO:  1.5543999870715197e-08

n:  50 
AVG Runtime:  8.202800017897971e-05 RATIO:  6.562240014318377e-10

n:  100 
AVG Runtime:  0.0001748864000546746 RATIO:  1.748864000546746e-10

n:  1000 
AVG Runtime:  0.0020294426001782996 RATIO:  2.0294426001782996e-12

n:  5000 
AVG Runtime:  0.009972029599884991 RATIO:  7.977623679907993e-14

"""