# 3. Solve problem 2; but use recursion instead of iteration.

def ordered_insert(a,n):
	if n<=1:
		return
	ordered_insert(a,n-1)
	x=a[n-1]
	j=n-2
	for i in range(n-1):
		if x<a[i]:
			t=x
			x=a[i]
			a[i]=t
	a[n-1]=x
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
