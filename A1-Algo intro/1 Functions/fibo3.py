#Memoized function
arr=[-1 for i in range(100)]
def fibM(n):
	if arr[n]==-1:
		if n==0:
			arr[0]=0
		elif n==1:
			arr[1]=1
		else:
			arr[n]=fibM(n-1)+fibM(n-2)
	return arr[n]

			
		
ch=1
while ch==1:
	n=int(input("Enter the value of n: "))
	print(n,"th term of the fibonacci series: ",fibM(n),"\n")
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
