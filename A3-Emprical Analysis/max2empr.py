"""Algorithm in Question 1 calculates the sum of each subarray in linear time (O(n)). By calculating the sums of all prefixes A[0:i] for 0 ≤ i ≤ n of the array once and saving them in a
table prefix sum, we can calculate sum(A, i, j in constant time, using
sum(A, i, j) = prefix_sum[j] - prefix_sum[i]
Design an algorithm max subarray sum quadratic using this idea and implement it. Show
that the algorithm runs in quadratic time, O(n
2
). Do empirical analysis of the algorithm."""
import random
import timeit
def  max_subarray_sum_quadratic(a):
	maxsum=0
	lindex=0
	hindex=0
	n=len(a)
	p=prefix_sum(a)
	for i in range(0,n-1):
		for j in range(i+1,n):
			subsum=sum(p,i,j)
			if subsum>maxsum:
				maxsum=subsum
				lindex=i
				hindex=j
	if a[n-1]>maxsum:
		maxsum=a[n-1]
		lindex=n-1
		hindex=n
	"""print("The input array is: ",a)
	print("The maximum subarray sum is: ",maxsum)
	print("The maximum sub array is: a[",lindex,":",hindex,"]")
	print(a[lindex:hindex],"\n\n")"""
	
def prefix_sum(a):
	psum=[0 for x in range(100000)]
	psum[0]=a[0]
	for i in range(1,len(a)):
		psum[i]=psum[i-1]+a[i]
	return psum
def sum(p,i,j):
	return p[j-1]-p[i-1]
def empr():
	n=[10,50,100,1000,5000]
	for i in range(5): #5 different input sizes
		sum=0
		a=[]
		for m in range(5): #m is taken as 5
			for j in range(n[i]):#to generate the list of size n
				a.append(random.randint(-100,100))
			start = timeit.default_timer()
			max_subarray_sum_quadratic(a)
			stop = timeit.default_timer()
			sum=sum+(stop-start)
		avg=sum/5
		ratio=avg/pow(n[i],3)
		print("\nn: ",n[i],"\nAVG Runtime: ",avg,"RATIO: ",ratio)


print("EMPRICAL ANALYSIS: ")	
empr()			

"""OUTPUT

EMPRICAL ANALYSIS: 

n:  10 
AVG Runtime:  0.0029179950000070677 RATIO:  2.9179950000070676e-06

n:  50 
AVG Runtime:  0.004418834400030392 RATIO:  3.535067520024313e-08

n:  100 
AVG Runtime:  0.01072960359992976 RATIO:  1.072960359992976e-08

n:  1000 
AVG Runtime:  0.9000359426000614 RATIO:  9.000359426000613e-10

n:  5000 
AVG Runtime:  22.56017674740001 RATIO:  1.8048141397920009e-10



"""