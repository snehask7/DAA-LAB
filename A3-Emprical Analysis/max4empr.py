"""4. Suppose an algorithm maintains the maximum suffix sum of all subarrays A[0:j] for 0 ≤
j ≤ n in a table suffix max. We can compute them in a single scan of the array.
suffix_max [j] = max (suffix_max [j-1]+A[j-1], 0)
2
Using table suffix max, we can compute the maximum subarray sum of A[0:j] in a single
scan of the array using
subarray_max (A, j) = max (subarray_max (A,j-1), suffix_max [j])
Construct algorithm max_subarray_sum_linear using this idea and implement it. Show that
the algorithm runs in linear time, O(n). Do empirical analysis of the algorithm."""

import random
import timeit

def max_subarray_sum_linear(a):
	maxsum=-10000
	suffix_max=[0 for i in range(len(a))]
	suffix_max[0]=a[0]
	for i in range(1,len(a)):
		suffix_max [i] = max (suffix_max [i-1]+a[i], 0)	
	return max(suffix_max)
def empr():
	n=[10,50,100,1000,5000]
	for i in range(5): #5 different input sizes
		sum=0
		a=[]
		for m in range(5): #m is taken as 5
			for j in range(n[i]):#to generate the list of size n
				a.append(random.randint(-100,100))
			start = timeit.default_timer()
			maxsum=max_subarray_sum_linear(a)
			stop = timeit.default_timer()
			sum=sum+(stop-start)
		avg=sum/5
		ratio=avg/pow(n[i],3)
		print("\nn: ",n[i],"\nAVG Runtime: ",avg,"RATIO: ",ratio)

print("EMPRICAL ANALYSIS: ")	
empr()	

"""
EMPRICAL ANALYSIS: 

n:  10 
AVG Runtime:  1.0042800022347365e-05 RATIO:  1.0042800022347365e-08

n:  50 
AVG Runtime:  3.964480010836269e-05 RATIO:  3.1715840086690154e-10

n:  100 
AVG Runtime:  7.950999997774488e-05 RATIO:  7.950999997774488e-11

n:  1000 
AVG Runtime:  0.0008776625999416865 RATIO:  8.776625999416865e-13

n:  5000 
AVG Runtime:  0.0039045524000357545 RATIO:  3.1236419200286037e-14

"""