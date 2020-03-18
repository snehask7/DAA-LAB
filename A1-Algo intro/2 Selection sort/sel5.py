"""Implement selection sort, using minimum() function. Note: remember that when a function changes the
items of an array parameter, the changes are effected in the items of the actual array argument also.
Test the function from a main() for several lists of numbers. Each test should read a list of
numbers from stdin."""

def minimum(a,low,high):
	x=len(a)
	minval=100000
	for i in range(low,high):
		if a[i]<minval:
			minval=a[i]
			index=i
	return index
def selsort(a,n):
	for i in range(0,n-1):
		small=minimum(a,i,n)
		temp=a[i]
		a[i]=a[small]
		a[small]=temp


def main():
	ch=1
	while ch!=2:
		n=int(input("Enter the number of elements in the array: "))
		a=[0 for i in range(n)]
		for i in range(n):
			a[i]=int(input("Enter the element: "))
		selsort(a,n)
		print("After sorting: ",a)
		
		ch=int(input("Enter 1 to continue and 2 to exit: "))
main()

"""
Enter the number of elements in the array: 6	
Enter the element: 77
Enter the element: 4
Enter the element: 987
Enter the element: 1
Enter the element: 112
Enter the element: 31
After sorting:  [1, 4, 31, 77, 112, 987]
Enter 1 to continue and 2 to exit: 2

"""
