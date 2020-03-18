"""Empirical analysis: Observe the running times of max subarray sum cubic for increasing
sizes of input. To observe the running time of a function for an input size n, call the function
m times with same input and take the average. For each input size, record the actual running time, and the ratio of the actual running time to its asymptotic running time in a table"""
import random
import timeit

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
	
def sum(a,i,j):
	sum=0
	for x in range(i,j):
		sum=sum+a[x]
	return sum
		
def empr():
	n=[10,50,100,1000,5000]
	for i in range(5): #5 different input sizes
		sum=0
		a=[]
		for m in range(5): #m is taken as 5
			for j in range(n[i]):#to generate the list of size n
				a.append(random.randint(-100,100))
			start = timeit.default_timer()
			max_subarray_sum_cubic(a)
			stop = timeit.default_timer()
			sum=sum+(stop-start)
		avg=sum/5
		ratio=avg/pow(n[i],3)
		print("\nn: ",n[i],"\nAVG Runtime: ",avg,"\nRATIO: ",ratio)

print("EMPRICAL ANALYSIS: ")	
empr()			
"""
EMPRICAL ANALYSIS: 

n:  10 
AVG Runtime:  0.00045885019999332145 
RATIO:  4.5885019999332146e-07

n:  50 
AVG Runtime:  0.041762627400021304 
RATIO:  3.3410101920017045e-07

n:  100 
AVG Runtime:  0.35054796379995423 
RATIO:  3.505479637999542e-07




"""
