"""5. You are given as input an array a[0:n] of n numbers. The output should be sorted a[0:n].
Break the problem into a[0:n-1] and a[n-1]. Sort a[0:n-1] recursively. Then, insert
a[n-1] in the right place in a[0:n-1] using ordered insert(a, n)."""


def ordered_insert(a,n):
	x=a[n-1]
	for i in range(n-1):
		if x<a[i]:
			t=x
			x=a[i]
			a[i]=t
	a[n-1]=x
def sort_array(a,n): 
	if n!=1:
		sort_array(a,n-1) 
		ordered_insert(a,n)
	else:	
		return

m=int(input("Enter the number of terms: "))
a=[]
for i in range(m):
	a.append(int(input("Enter a number: ")))

sort_array(a,m)
print(a)

"""
OUTPUT

Enter the number of terms: 5
Enter a number: 34
Enter a number: 2
Enter a number: 545
Enter a number: 1
Enter a number: 12
[1, 2, 12, 34, 545]

"""
