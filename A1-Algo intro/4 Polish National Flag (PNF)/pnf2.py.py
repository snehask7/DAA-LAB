"""Input is an array of items a[low:high]. Modify the function PNF(a, low, high) that selects a[low] as a pivot and partitions the array into two subarrays a[low:i] and a[i:high]
such that all the items smaller than the pivot form [low:i], and all the other items form
[i:n]."""

def PNF(a,low,high):
	piv=a[low]
	x=low+1
	while a[x]<piv:
		x=x+1
	i=x
	print(a[low:i])
	print(a[i:n])
ch=1
while ch!=2:
	n=int(input("Enter the number of elements in the array: "))
	a=[0 for i in range(n)]
	for i in range(n):
		a[i]=int(input("Enter the element: "))
	low=int(input("Enter the low index: "))
	high=int(input("Enter the high index: "))
	PNF(a,low,high)
	ch=int(input("Enter 1 to continue and 2 to exit: "))

	"""
	OUTPUT

	Enter the number of elements in the array: 8
	Enter the element: 4
	Enter the element: 3
	Enter the element: 7
	Enter the element: 5
	Enter the element: 4
	Enter the element: 3
	Enter the element: 9
	Enter the element: 10
	Enter the low index: 2
	Enter the high index: 7
	[7, 5, 4, 3]
	[9, 10]
	Enter 1 to continue and 2 to exit: 2

	"""