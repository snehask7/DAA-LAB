"""2. In Quicksort, we choose a pivot and partition a subarray into two smaller subarrays, one
smaller than the pivot and the other larger than or equal to the pivot.
Since we cannot directly compare two nuts (or two bolts), we cannot use the standard par-
tition algorithm. Choose a pivot bolt, and partition the nuts into two subsets, one subset
smaller than the pivot bolt and the other larger than the pivot bolt (not larger than or equal,
since the nuts are all distinct in size). Now we have the pivot nut in its final position. Now,
using the pivot nut, partition the bolts. After these 2n − 1 tests, we have one matched pair,
and the remaining nuts and bolts are partitioned into two subsets: those smaller than the
pivot pair and those larger than the pivot pair. Construct the algorithm to partition nuts
and bolts. Implement it."""

def partition(arr,p, l, r):
	j = l
	for i in range(l, r+1):
		if(arr[i]<p):
			arr[j],arr[i]=arr[i],arr[j]
			j+=1
	for i in range(l, r+1):
		if arr[i]==p:
			arr[i],arr[j]=arr[j],arr[i]
			break
	return j#technically not needed
def quicksort(nuts, bolts, l, r):
	if l<r:
		pivot=partition(nuts, bolts[r], l, r)
		#partition(bolts, bolts[r], l, r)
		pivot=partition(bolts, nuts[pivot], l, r)
		quicksort(nuts, bolts, l, pivot-1)
		quicksort(nuts, bolts, pivot+1, r)


n=int(input("Enter the number of nut and bolt pairs: "))
print("Enter the sizes of nuts: ")
nuts=[int(i) for i in input().split()]
print("Enter the sizes of bolts: ")
bolts=[int(i) for i in input().split()]
quicksort(nuts, bolts, 0, n-1)
print(nuts)
print(bolts)

"""
OUTPUT

Enter the number of nut and bolt pairs: 5
Enter the sizes of nuts: 
5 4 3 2 1
Enter the sizes of bolts: 
3 4 1 2 5
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

"""
