"""6. The input is an array of N numbers. The array is sorted in ascending order except for the
first number (that at 0), which may be out of order. The output should be a sorted array of N
original numbers which include the out-of-order number."""

def ordered_insert(a):
	n=len(a)
	for i in range(1,n):
		if a[i-1]>a[i]:
			t=a[i-1]
			a[i-1]=a[i]
			a[i]=t
n=int(input("Enter the number of terms: "))
a=[]
for i in range(n):
	a.append(int(input("Enter a number: ")))
ordered_insert(a)
print(a)


"""
OUTPUT

Enter the number of terms: 5
Enter a number: 6
Enter a number: 1
Enter a number: 2
Enter a number: 8
Enter a number: 9
[1, 2, 6, 8, 9]

"""
