"""4. Solve problem 2, but use a slighly different iterative step: back up a[n-1] in a variable. Then
keep shifting the items of the array to the right until the correct position for the out-of-order
item is found; then, in that position, insert the out-of-order item from its backup variable."""
def ordered_insert(a,n):
	x=a[n-1]
	i=n-2
	while i>=0:
		if a[i]>x:
			a[i+1]=a[i]
		else:
			break

		i=i-1
	a[i+1]=x
m=int(input("Enter the number of terms: "))
a=[]
for i in range(m):
	a.append(int(input("Enter a number: ")))
n=int(input("Enter the value of n: "))
ordered_insert(a,n)
print(a)

"""
Enter the number of terms: 6
Enter a number: 1
Enter a number: 4
Enter a number: 7
Enter a number: 2
Enter a number: 9
Enter a number: 10
Enter the value of n: 4
[1, 2, 4, 7, 9, 10]

"""
