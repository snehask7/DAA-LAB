"""3.  Write a function minimum(a) that finds the smallest number in an array a. Input is an array a[0:n] of n comparable items. Output should be the index of the smallest item a[0:n]. Test the function interactively and from a main() function.  Test it for several lists of numbers
where each test should read a list of numbers from the keyboard."""

def minimum(a):
	x=len(a)
	minval=100000
	for i in range(x):
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
		print("The index of the smallest element in the list is: ",minimum(a))
		ch=int(input("Enter 1 to continue and 2 to exit: "))
main()

			
"""
OUTPUT

Enter the number of elements in the array: 7
Enter the element: 234
Enter the element: 54
Enter the element: 77
Enter the element: 66
Enter the element: 4
Enter the element: 56
Enter the element: 768
The index of the smallest element in the list is:  4
Enter 1 to continue and 2 to exit: 1
Enter the number of elements in the array: 5 
Enter the element: 34
Enter the element: 2
Enter the element: 567
Enter the element: 5666
Enter the element: 77
The index of the smallest element in the list is:  1
Enter 1 to continue and 2 to exit: 2

"""
