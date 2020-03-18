#Recursive method
def fibR(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibR(n-1)+fibR(n-2)
ch=1
while ch==1:
	n=int(input("Enter the value of n: "))
	print(n,"th term of the fibonacci series: ",fibR(n),"\n")
	ch=int(input("Enter 1 to continue and 2 to exit: "))
#Memoized function
def fibR(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibR(n-1)+fibR(n-2)
ch=1
while ch==1:
	n=int(input("Enter the value of n: "))
	print(n,"th term of the fibonacci series: ",fibR(n),"\n")
	ch=int(input("Enter 1 to continue and 2 to exit: "))
"""
OUTPUT

Enter the value of n: 6
6 th term of the fibonacci series:  8 

Enter 1 to continue and 2 to exit: 1
Enter the value of n: 5
5 th term of the fibonacci series:  5 

Enter 1 to continue and 2 to exit: 1
Enter the value of n: 4
4 th term of the fibonacci series:  3 

Enter 1 to continue and 2 to exit: 1
Enter the value of n: 3
3 th term of the fibonacci series:  2 

Enter 1 to continue and 2 to exit: 1
Enter the value of n: 2
2 th term of the fibonacci series:  1 

Enter 1 to continue and 2 to exit: 1
Enter the value of n: 1
1 th term of the fibonacci series:  1 

Enter 1 to continue and 2 to exit: 1
Enter the value of n: 0
0 th term of the fibonacci series:  0 

Enter 1 to continue and 2 to exit: 2

"""
