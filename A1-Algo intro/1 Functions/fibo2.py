#Iterative method
def fibI(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		x=0
		y=1
		for i in range(2,n+1):
			fibo=x+y
			x=y
			y=fibo
		return fibo
ch=1
while ch==1:
	n=int(input("Enter the value of n: "))
	print(n,"th term of the fibonacci series: ",fibI(n),"\n")
	ch=int(input("Enter 1 to continue and 2 to exit: "))

