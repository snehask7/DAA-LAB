"""7. The input is an array of whole numbers. The numbers are stored only at positions 1, 2, 4,
8, 16, ... (powers of 2). We do not store anything in between. The elements of the array are
sorted except the element at position 1. Rearrange the numbers so that the elements of the
array are sorted."""

def ordered_insert(a,n):
	for i in range(1,n):
		if a[pow(2,i-1)]>a[pow(2,i)]:
			t=a[pow(2,i-1)]
			a[pow(2,i-1)]=a[pow(2,i)]
			a[pow(2,i)]=t
n=int(input("Enter the number of terms: "))
a=[0 for i in range (pow(2,n))]
for i in range(n):
	a[pow(2,i)]=int(input("Enter number: "))
ordered_insert(a,n)
for i in range(n):
	print(a[pow(2,i)])

"""
Enter the number of terms: 5
Enter number: 5
Enter number: 2
Enter number: 4
Enter number: 8
Enter number: 9
2
4
5
8
9
"""
