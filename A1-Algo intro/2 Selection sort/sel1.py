#Selection sort q1
def print_array(a,low,high):
	print(a[low:high])
n=int(input("Enter the number of terms in the array: "))
a=[]
for i in range(n):
	x=int(input("Enter the element to add: "))
	a.append(x)
low=int(input("Enter the low index: "))
high=int(input("Enter the high index: "))
print_array(a,low,high)

"""
OUTPUT

Enter the number of terms in the array: 7
Enter the element to add: 2
Enter the element to add: 4
Enter the element to add: 76
Enter the element to add: 97
Enter the element to add: 545
Enter the element to add: 2
Enter the element to add: 4
Enter the low index: 3
Enter the high index: 6
[97, 545, 2]

"""
