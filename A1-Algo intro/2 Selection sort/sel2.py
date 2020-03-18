""" Write a function readarray(a) to read a list of integers from the keyboard into the subarray a[0:n] and return n, the number of integers read. Since the caller of readarray(a) does not know in advance how many numbers would be read by read array(a), the caller should pass a sufficiently large a"""

def readarray(a):
	n=0
	print("Enter -777 to terminate!")
	x=0
	while True:
		x=int(input("Enter the number: "))
		if x==-777:
			break		
		else:
			a[n]=x
			n=n+1

	return n
arr=[0 for i in range(10000)]
print("The value of n is: ",readarray(arr))

"""
OUTPUT

Enter -777 to terminate!
Enter the number: 4
Enter the number: 6
Enter the number: 8
Enter the number: 99
Enter the number: 2345
Enter the number: -777
The value of n is:  5

"""
