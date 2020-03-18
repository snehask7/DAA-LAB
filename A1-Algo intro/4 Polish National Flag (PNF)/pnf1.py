"""You are given an array of items a[low:high], each of which is either positive or negative. Define a function PNF(a, low, high) that partitions the array into two subarrays a[low:i]
and a[i:high] such that all the negative items of the array form [low:i], and all the positive items form [i:n]. Test the function from main(). Use several lists of numbers for
testing. (Note: We will use this algorithm for implementing quicksort().)"""

def PNF(a,low,high):
	x=low
	while x<high:
		if a[x]>=0:
			i=x
			break
		x=x+1
	print(a[low:i])
	print(a[i:high])
def main():
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

main()

"""
OUTPUT


Enter the number of elements in the array: 8
Enter the element: -2
Enter the element: -3
Enter the element: -4
Enter the element: -5
Enter the element: 3
Enter the element: 4
Enter the element: 5
Enter the element: 6
Enter the low index: 2
Enter the high index: 8
[-4, -5]
[3, 4, 5, 6]
Enter 1 to continue and 2 to exit: 1
Enter the number of elements in the array: 6
Enter the element: -2
Enter the element: -3
Enter the element: -4
Enter the element: 6
Enter the element: 7
Enter the element: 8
Enter the low index: 1
Enter the high index: 5 
[-3, -4]
[6, 7]
Enter 1 to continue and 2 to exit: 2  
"""