""" 1. The input to function ordered_insert(a) is an array a[0:n] of n integers. The precondition is: the items of the array are in non-decreasing
 (ascending) order except the last item (that at n-1) which may be out of order. The postcondition is that a[0:n] is sorted, that is, the out-of-order 
 item has been brought to its right position. Use this iterative step: keep swapping the out-of-order item until it comes to the “right” position, that is, 
 ordered with its neighbors. """

def ordered_insert(a):
	n=len(a)
	x=a[n-1]
	for i in range(n-1):
		if x<a[i]:
			t=x
			x=a[i]
			a[i]=t
	a[n-1]=x
n=int(input("Enter the number of terms: "))
a=[]
for i in range(n):
	a.append(int(input("Enter a number: ")))
ordered_insert(a)
print(a)

"""
OUTPUT

Enter the number of terms: 5
Enter a number: 3
Enter a number: 5
Enter a number: 8
Enter a number: 11
Enter a number: 4
[3, 4, 5, 8, 11]

"""
