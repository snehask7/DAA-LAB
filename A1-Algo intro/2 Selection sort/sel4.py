"""Modify minimum(a) to minimum(a, low, high) . You are given an array a[0:n] of n com- parable items.  Define the function minimum(a, low,high)
that returns the index of the smallest item in the subarray a[low:high]."""

def minimum(a,low,high):
	x=len(a)
	minval=100000
	for i in range(low,high):
		if a[i]<minval:
			minval=a[i]
			index=i
	return index
def main():
	ch=1
	while ch!=2:
		n=int(input("Enter the number of elements in the array: "))
		a=[0 for i in range(n)]
		for i in range(n):
			a[i]=int(input("Enter the element: "))
		low=int(input("Enter the low index: "))
		high=int(input("Enter the high index: "))
		print("The index of the smallest element in the list is: ",minimum(a,low,high))
		ch=int(input("Enter 1 to continue and 2 to exit: "))
main()

"""
Enter the number of elements in the array: 5
Enter the element: 45
Enter the element: 2
Enter the element: 56
Enter the element: 99
Enter the element: 1
Enter the low index: 1
Enter the high index: 4
The index of the smallest element in the list is:  1
Enter 1 to continue and 2 to exit: 2

"""
